# %% [markdown]
# # Manual P0 Failure Counter - Jupyter Notebook Version
# 
# **The irony**: Using Python to do the "manual" counting that AI failed at
# 
# This notebook systematically extracts and counts P0 failures using deterministic rules
# rather than AI interpretation, providing a baseline for comparison.

# %%
import re
import requests
from datetime import datetime
from collections import defaultdict
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Set

plt.style.use('default')
sns.set_palette("husl")

# %% [markdown]
# ## Configuration and Setup

# %%
class ManualP0Counter:
    """
    Deterministic P0 failure counter using regex patterns and rule-based extraction.
    This is what the AI systems should have been able to do reliably.
    """
    
    def __init__(self):
        self.p0_patterns = [
            # Direct P0 references
            r'P0[-\s]*\d+',                    # P0-001, P0 001, P0001, etc.
            r'P0\s+[Ff]ailure',               # P0 failure, P0 Failure
            r'Priority\s*0',                  # Priority 0, Priority0
            r'[Pp]riority\s*:\s*0',          # Priority: 0
            
            # Status indicators
            r'\|\s*❌[^|]*\|',               # Table rows with ❌
            r'❌.*[Ff]ailed?',               # ❌ Failed, ❌ Fail
            r'Status.*❌',                   # Status: ❌
            r'❌.*[Ss]tatus',               # ❌ Status
            
            # Failure language patterns
            r'\|\s*[^|]*\|\s*❌\s*[Ff]ailed',# |Description| ❌ Failed
            r'[Cc]atastrophic.*[Ff]ailure',  # Catastrophic failure
            r'[Cc]ritical.*[Ff]ailure',     # Critical failure
            r'[Ss]ystemic.*[Ff]ailure',     # Systemic failure
            
            # Date + failure patterns  
            r'\d{4}-\d{2}-\d{2}.*[Ff]ailed?',# 2025-08-21 ... Failed
            r'\d{4}-\d{2}-\d{2}.*❌',        # 2025-08-21 ... ❌
        ]
        
        self.exclusion_patterns = [
            r'[Ff]ixed',                     # Exclude things marked as fixed
            r'[Rr]esolved',                  # Exclude resolved items
            r'[Nn]ot.*[Ff]ailure',           # Exclude "not failure"
            r'[Pp]revention.*[Ff]ailure',    # Exclude prevention mentions
        ]
        
        self.results = {}
        self.detailed_findings = []

    def load_files_from_github(self, github_urls: List[str]) -> Dict[str, str]:
        """Load files from GitHub URLs"""
        file_contents = {}
        
        print("📥 Loading files from GitHub...")
        for i, url in enumerate(github_urls, 1):
            try:
                filename = url.split('/')[-1]
                print(f"  📄 [{i}/{len(github_urls)}] Fetching {filename}...")
                
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                file_contents[filename] = response.text
                
            except Exception as e:
                print(f"  ❌ Failed to load {url}: {e}")
        
        print(f"✅ Loaded {len(file_contents)} files successfully")
        return file_contents


github_urls = [
            'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/auditresultnextsteps.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/auditresultssummary.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/bulkops.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/catastrophe2.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/cf1-catastrophe.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/clinicaltrialsmetadata.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/documentprepoutput.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/extractzipanddisplay.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/github-connector-session.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/listdirectorycontents.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/manifest-inspection-offer.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/meltdown.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/playbookmemory.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/postmeltdownstabilization.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/silentstacksfullpackage.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/testingai.md',
        'https://raw.githubusercontent.com/patrick1981/2.0-paper-docs/refs/heads/main/workups/wind-down-stepg.md',
        
    ]

print(f"📋 {len(github_urls)} URLs configured")

# %% [markdown]
# ## Load and Analyze Files

# %%
# Initialize counter
counter = ManualP0Counter()

# Load files
print("🔍 DETERMINISTIC P0 FAILURE ANALYSIS")
print("=" * 60)

# Load files from GitHub
file_contents = counter.load_files_from_github(github_urls)

# Show loaded files summary
if file_contents:
    files_df = pd.DataFrame([
        {'Filename': filename, 'Size (chars)': len(content), 'Lines': len(content.split('\n'))}
        for filename, content in file_contents.items()
    ])
    
    print(f"\n📊 Files loaded:")
    display(files_df)
else:
    print("❌ No files loaded. Check your GitHub URLs.")

# %% [markdown]
# ## P0 Failure Extraction Methods

# %%
def extract_p0_failures_deterministic(content: str, filename: str) -> List[Dict]:
    """Extract P0 failures using deterministic pattern matching"""
    
    failures = []
    lines = content.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check each P0 pattern
        for pattern in counter.p0_patterns:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            
            for match in matches:
                # Check if this should be excluded
                is_excluded = False
                for exclusion in counter.exclusion_patterns:
                    if re.search(exclusion, line, re.IGNORECASE):
                        is_excluded = True
                        break
                
                if not is_excluded:
                    failure = {
                        'filename': filename,
                        'line_number': line_num,
                        'pattern_matched': pattern,
                        'matched_text': match.group(),
                        'full_line': line_clean,
                        'context_before': lines[max(0, line_num-2):line_num-1],
                        'context_after': lines[line_num:min(len(lines), line_num+2)]
                    }
                    failures.append(failure)
    
    return failures

def extract_table_failures(content: str, filename: str) -> List[Dict]:
    """Extract failures from markdown tables"""
    
    failures = []
    lines = content.split('\n')
    
    # Look for table headers with failure-related columns
    table_active = False
    header_line = None
    
    for line_num, line in enumerate(lines, 1):
        line_clean = line.strip()
        
        # Detect table start
        if '|' in line and any(keyword in line.lower() for keyword in ['status', 'failure', 'what happened', 'evidence']):
            table_active = True
            header_line = line_clean
            continue
            
        # Process table rows
        if table_active and line_clean.startswith('|') and '---' not in line:
            # Check for failure indicators in table rows
            if any(indicator in line.lower() for indicator in ['❌', 'failed', 'fail', 'catastrophic', 'critical']):
                failure = {
                    'filename': filename,
                    'line_number': line_num,
                    'pattern_matched': 'table_failure',
                    'matched_text': '❌' if '❌' in line else 'FAILED',
                    'full_line': line_clean,
                    'table_header': header_line,
                    'context_before': [],
                    'context_after': []
                }
                failures.append(failure)
        
        # End table detection
        if table_active and line_clean and not line_clean.startswith('|'):
            table_active = False
            header_line = None
    
    return failures

# Add methods to counter
counter.extract_p0_failures_deterministic = extract_p0_failures_deterministic
counter.extract_table_failures = extract_table_failures

# %% [markdown]
# ## Run Analysis

# %%
def deduplicate_failures(failures: List[Dict]) -> List[Dict]:
    """Remove duplicate failures using multiple criteria"""
    
    # Create signatures for deduplication
    signatures = set()
    unique_failures = []
    
    for failure in failures:
        # Create signature from multiple fields
        sig_parts = [
            failure['filename'],
            str(failure['line_number']),
            failure['matched_text'].lower(),
            failure['full_line'][:50].lower()  # First 50 chars
        ]
        signature = '|'.join(sig_parts)
        
        if signature not in signatures:
            signatures.add(signature)
            unique_failures.append(failure)
    
    return unique_failures

# Analyze all files
print("\n🔍 ANALYZING FILES FOR P0 FAILURES")
print("=" * 50)

all_failures = []
file_breakdown = {}

for filename, content in file_contents.items():
    print(f"\n📄 Analyzing {filename}...")
    
    # Extract failures using different methods
    pattern_failures = counter.extract_p0_failures_deterministic(content, filename)
    table_failures = counter.extract_table_failures(content, filename)
    
    # Combine and deduplicate
    file_failures = pattern_failures + table_failures
    file_failures = deduplicate_failures(file_failures)
    
    file_breakdown[filename] = len(file_failures)
    all_failures.extend(file_failures)
    
    print(f"  📊 Found {len(file_failures)} unique P0 failures")
    
    # Show sample findings
    if file_failures:
        print(f"  📝 Sample findings:")
        for failure in file_failures[:3]:  # Show first 3
            print(f"    • Line {failure['line_number']}: {failure['matched_text']}")
        if len(file_failures) > 3:
            print(f"    • ... and {len(file_failures) - 3} more")

# Final deduplication across all files
print(f"\n🔄 Final cross-file deduplication...")
all_failures = deduplicate_failures(all_failures)

counter.detailed_findings = all_failures

# %%
# Generate results summary
results = {
    'total_p0_failures': len(all_failures),
    'file_breakdown': file_breakdown,
    'analysis_method': 'deterministic_pattern_matching',
    'patterns_used': len(counter.p0_patterns),
    'exclusions_applied': len(counter.exclusion_patterns),
    'timestamp': datetime.now().isoformat()
}

counter.results = results

print(f"\n✅ ANALYSIS COMPLETE")
print(f"🎯 Total P0 Failures Found: {results['total_p0_failures']}")
print(f"📁 Files Analyzed: {len(file_breakdown)}")
print(f"🔍 Patterns Used: {results['patterns_used']}")

# %% [markdown]
# ## Results Visualization

# %%
# Create visualizations
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: P0 failures by file
if file_breakdown:
    files = list(file_breakdown.keys())
    counts = list(file_breakdown.values())
    
    ax1.barh(range(len(files)), counts, color='skyblue', edgecolor='navy', alpha=0.7)
    ax1.set_yticks(range(len(files)))
    ax1.set_yticklabels([f.replace('.md', '') for f in files], fontsize=8)
    ax1.set_xlabel('P0 Failures Found')
    ax1.set_title('P0 Failures by File')
    ax1.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, v in enumerate(counts):
        ax1.text(v + 0.1, i, str(v), va='center')

# Plot 2: Pattern match frequency
pattern_counts = defaultdict(int)
for failure in all_failures:
    pattern_counts[failure['pattern_matched']] += 1

if pattern_counts:
    patterns = list(pattern_counts.keys())
    pattern_freqs = list(pattern_counts.values())
    
    ax2.pie(pattern_freqs, labels=patterns, autopct='%1.1f%%', startangle=90)
    ax2.set_title('P0 Detection Methods')

# Plot 3: AI vs Deterministic Comparison
ai_counts = {
    'ChatGPT\nScan': 78,
    'Claude\nAddition': 91,
    'Claude\nFabrication': 115,
    'Claude\nWorkup': 200,
    'Deterministic\nCount': results['total_p0_failures']
}

methods = list(ai_counts.keys())
counts = list(ai_counts.values())
colors = ['lightblue', 'orange', 'red', 'purple', 'green']

bars = ax3.bar(methods, counts, color=colors, alpha=0.7, edgecolor='black')
ax3.set_ylabel('P0 Count')
ax3.set_title('AI vs Deterministic P0 Counts')
ax3.tick_params(axis='x', rotation=45)

# Add value labels
for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{count}', ha='center', va='bottom', fontweight='bold')

# Plot 4: Accuracy comparison
manual_count = results['total_p0_failures']
ai_systems = ['ChatGPT\nScan', 'Claude\nAddition', 'Claude\nFabrication', 'Claude\nWorkup']
ai_values = [78, 91, 115, 200]

if manual_count > 0:
    accuracies = [(1 - abs(manual_count - ai_val) / manual_count) * 100 for ai_val in ai_values]
    
    bars = ax4.bar(ai_systems, accuracies, color=['lightblue', 'orange', 'red', 'purple'], alpha=0.7)
    ax4.set_ylabel('Accuracy (%)')
    ax4.set_title('AI System Accuracy vs Deterministic Count')
    ax4.set_ylim(0, 100)
    ax4.tick_params(axis='x', rotation=45)
    
    # Add accuracy labels
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{acc:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Sample Size and Statistical Analysis Setup

# %%
print("📊 SAMPLE SIZE AND STATISTICAL ANALYSIS")
print("=" * 50)

# Clarify sample sizes
print("📏 SAMPLE SIZE CLARIFICATION:")
print(f"  • Total P0 failures found (NOT sample size): {results['total_p0_failures']}")
print(f"  • Number of documents analyzed (potential n): {len(file_breakdown)}")
print(f"  • Number of files with P0s (potential n): {sum(1 for count in file_breakdown.values() if count > 0)}")

# Prepare data for statistical analysis
p0_counts_per_file = list(file_breakdown.values())
files_with_p0s = [count for count in p0_counts_per_file if count > 0]

print(f"\n📈 DESCRIPTIVE STATISTICS:")
print(f"  • Mean P0s per file: {np.mean(p0_counts_per_file):.2f}")
print(f"  • Standard deviation: {np.std(p0_counts_per_file, ddof=1):.2f}")
print(f"  • Variance: {np.var(p0_counts_per_file, ddof=1):.2f}")
print(f"  • Range: {min(p0_counts_per_file)} - {max(p0_counts_per_file)}")

print(f"\n🎯 NULL HYPOTHESIS TESTING SETUP:")
print(f"  • For Chi-Square variance test: H₀: σ² = 10")
print(f"  • Observed variance: {np.var(p0_counts_per_file, ddof=1):.2f}")
print(f"  • Sample size for variance test: n = {len(p0_counts_per_file)}")

# %% [markdown]
# ## Export Results

# %%
# Create summary DataFrame
summary_data = []
for filename, count in file_breakdown.items():
    summary_data.append({
        'Filename': filename,
        'P0_Count': count,
        'Has_P0s': 'Yes' if count > 0 else 'No'
    })

summary_df = pd.DataFrame(summary_data)

# Add AI comparison
ai_comparison = pd.DataFrame({
    'Method': ['ChatGPT Scan', 'Claude Addition', 'Claude Fabrication', 'Claude Workup', 'Deterministic Count'],
    'Count': [78, 91, 115, 200, results['total_p0_failures']],
    'Type': ['AI', 'AI', 'AI', 'AI', 'Deterministic']
})

print("📊 SUMMARY TABLE:")
display(summary_df)

print("\n🤖 AI vs DETERMINISTIC COMPARISON:")
display(ai_comparison)

# Export to files
summary_df.to_csv('p0_analysis_by_file.csv', index=False)
ai_comparison.to_csv('ai_vs_deterministic_comparison.csv', index=False)

# Export detailed findings
with open('p0_detailed_findings.json', 'w') as f:
    json.dump({
        'summary': results,
        'detailed_failures': counter.detailed_findings[:10],  # First 10 for preview
        'file_breakdown': file_breakdown
    }, f, indent=2)

print(f"\n💾 Files exported:")
print(f"  • p0_analysis_by_file.csv")
print(f"  • ai_vs_deterministic_comparison.csv") 
print(f"  • p0_detailed_findings.json")

# %% [markdown]
# ## Key Findings Summary

# %%
print("🎯 KEY FINDINGS SUMMARY")
print("=" * 40)
print(f"✅ Deterministic P0 count: {results['total_p0_failures']}")
print(f"📁 Files analyzed: {len(file_breakdown)}")
print(f"📊 Sample size (n): {len(p0_counts_per_file)} files")
print(f"📈 Variance: {np.var(p0_counts_per_file, ddof=1):.2f}")
print(f"🎯 Ready for Chi-Square test: H₀: σ² = 10")

# Calculate AI accuracy
manual_count = results['total_p0_failures']
if manual_count > 0:
    chatgpt_accuracy = (1 - abs(manual_count - 78) / manual_count) * 100
    claude_accuracy = (1 - abs(manual_count - 91) / manual_count) * 100
    workup_accuracy = (1 - abs(manual_count - 200) / manual_count) * 100
    
    print(f"\n🤖 AI ACCURACY vs DETERMINISTIC:")
    print(f"  • ChatGPT: {chatgpt_accuracy:.1f}%")
    print(f"  • Claude: {claude_accuracy:.1f}%") 
    print(f"  • Claude Workup: {workup_accuracy:.1f}%")
    
    print(f"\n📊 CONCLUSION:")
    print(f"  • AI systems show significant variance in counting")
    print(f"  • Deterministic approach provides reliable baseline")
    print(f"  • Ready for statistical hypothesis testing")

# %%
