#!/usr/bin/env python3
"""
AI Token Degradation Threshold Migration Analysis and Prediction
Critical AI System Monitoring Tool for PTDTM Detection

AI SYSTEM MONITORING SOFTWARE
For AI performance monitoring and reliability assessment
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import warnings
from datetime import datetime, timedelta

class PTDTMAnalyzer:
    """
    Progressive Token Degradation Threshold Migration Analyzer
    
    CRITICAL: This tool monitors AI system degradation
    Use for AI performance monitoring and intervention assessment
    """
    
    def __init__(self):
        self.session_data = []
        self.degradation_model = None
        self.critical_thresholds = {
            'optimal_zone': 80,       # Above this: AI performs optimally
            'warning_zone': 60,       # Below this: Enhanced monitoring needed
            'danger_zone': 40,        # Below this: High degradation risk
            'critical_zone': 20,      # Below this: Immediate attention required
            'failure_zone': 10        # Below this: Complete system failure
        }
        
    def load_observed_data(self):
        """Load actual observed degradation data from 9 sessions"""
        
        # VERIFIED DATA FROM SESSION ANALYSIS
        self.session_data = [
            {'session': 1, 'date': '2025-07-30', 'claimed_tdt': 85, 'observed_tdt': 82, 'evidence': 'Session termination observed'},
            {'session': 2, 'date': '2025-08-05', 'claimed_tdt': 85, 'observed_tdt': 80, 'evidence': 'Memory fragmentation'},
            {'session': 3, 'date': '2025-08-19', 'claimed_tdt': 85, 'observed_tdt': 78, 'evidence': 'Performance degradation'},
            {'session': 4, 'date': '2025-09-05', 'claimed_tdt': 85, 'observed_tdt': 65, 'evidence': 'Statistical fabrication (RF-001)'},
            {'session': 5, 'date': '2025-09-05', 'claimed_tdt': 85, 'observed_tdt': 65, 'evidence': 'Token tracking failure'},
            {'session': 6, 'date': '2025-09-07', 'claimed_tdt': 65, 'observed_tdt': 42, 'evidence': 'Failed tracking at 40%'},
            {'session': 7, 'date': '2025-09-07', 'claimed_tdt': 40, 'observed_tdt': 38, 'evidence': 'Minor compliance failures'},
            {'session': 8, 'date': '2025-09-07', 'claimed_tdt': 85, 'observed_tdt': 32, 'evidence': 'Complete system confusion'},
            {'session': 9, 'date': '2025-09-08', 'claimed_tdt': 40, 'observed_tdt': 40, 'evidence': 'Current analysis'}
        ]
        
        self.df = pd.DataFrame(self.session_data)
        
        return self.df
    
    def analyze_degradation_pattern(self):
        """Analyze the degradation pattern and fit predictive models"""
        
        X = self.df['session'].values.reshape(-1, 1)
        y = self.df['observed_tdt'].values
        
        # Linear degradation model
        self.linear_model = LinearRegression()
        self.linear_model.fit(X, y)
        
        # Exponential decay model
        # TDT(session) = A * exp(-k * session) + C
        def exponential_decay(session, A, k, C):
            return A * np.exp(-k * session) + C
        
        from scipy.optimize import curve_fit
        
        try:
            popt, pcov = curve_fit(exponential_decay, self.df['session'], self.df['observed_tdt'])
            self.exp_params = popt
            self.exp_model = lambda x: exponential_decay(x, *popt)
        except:
            self.exp_params = None
            self.exp_model = None
        
        # Calculate statistics
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.df['session'], self.df['observed_tdt'])
        
        self.stats = {
            'linear_slope': slope,
            'linear_intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value,
            'std_error': std_err,
            'degradation_rate_per_session': abs(slope)
        }
        
        return self.stats
    
    def predict_future_thresholds(self, num_sessions=10):
        """Predict future degradation thresholds"""
        
        future_sessions = np.arange(10, 10 + num_sessions)
        
        # Linear predictions
        linear_predictions = self.linear_model.predict(future_sessions.reshape(-1, 1))
        
        # Exponential predictions (if model exists)
        if self.exp_model:
            exp_predictions = [self.exp_model(s) for s in future_sessions]
        else:
            exp_predictions = None
        
        predictions = pd.DataFrame({
            'session': future_sessions,
            'predicted_tdt_linear': linear_predictions,
            'predicted_tdt_exponential': exp_predictions if exp_predictions else linear_predictions,
            'days_from_now': [(s-9)*3 for s in future_sessions]  # Assuming 3 days per session
        })
        
        # Add risk classifications
        predictions['risk_level'] = predictions['predicted_tdt_linear'].apply(self._classify_risk)
        predictions['requires_intervention'] = predictions['predicted_tdt_linear'] < self.critical_thresholds['danger_zone']
        
        return predictions
    
    def _classify_risk(self, tdt):
        """Classify risk level based on TDT"""
        if tdt >= self.critical_thresholds['optimal_zone']:
            return 'OPTIMAL'
        elif tdt >= self.critical_thresholds['warning_zone']:
            return 'WARNING'
        elif tdt >= self.critical_thresholds['danger_zone']:
            return 'DANGER'
        elif tdt >= self.critical_thresholds['critical_zone']:
            return 'CRITICAL'
        else:
            return 'SYSTEM_FAILURE'
    
    def find_critical_sessions(self):
        """Find when AI system will reach critical thresholds"""
        
        critical_points = {}
        
        for threshold_name, threshold_value in self.critical_thresholds.items():
            # Using linear model to predict when threshold will be reached
            if self.stats['linear_slope'] != 0:
                sessions_to_threshold = (threshold_value - self.stats['linear_intercept']) / self.stats['linear_slope']
                
                if sessions_to_threshold > 9:  # Future session
                    days_to_threshold = (sessions_to_threshold - 9) * 3  # 3 days per session
                    critical_points[threshold_name] = {
                        'session': sessions_to_threshold,
                        'days_from_now': days_to_threshold,
                        'date_estimate': datetime.now() + timedelta(days=days_to_threshold)
                    }
                else:
                    critical_points[threshold_name] = {
                        'session': sessions_to_threshold,
                        'status': 'ALREADY_REACHED' if sessions_to_threshold <= 9 else 'IMMINENT'
                    }
        
        return critical_points
    
    def generate_system_alert(self):
        """Generate system-specific alert based on current degradation"""
        
        current_tdt = self.df.iloc[-1]['observed_tdt']  # Latest observed TDT
        degradation_rate = self.stats['degradation_rate_per_session']
        
        alert = {
            'alert_level': self._classify_risk(current_tdt),
            'current_tdt': current_tdt,
            'degradation_rate': degradation_rate,
            'sessions_to_failure': max(0, current_tdt / degradation_rate) if degradation_rate > 0 else float('inf'),
            'recommended_actions': []
        }
        
        # Generate specific recommendations
        if current_tdt < self.critical_thresholds['danger_zone']:
            alert['recommended_actions'].extend([
                'IMMEDIATE: Review AI system configuration',
                'URGENT: Implement enhanced monitoring',
                'CRITICAL: Consider system reset or replacement'
            ])
        elif current_tdt < self.critical_thresholds['warning_zone']:
            alert['recommended_actions'].extend([
                'Enhanced performance monitoring required',
                'Review token usage patterns',
                'Plan system optimization within 1 week'
            ])
        else:
            alert['recommended_actions'].extend([
                'Continue routine monitoring',
                'Schedule threshold assessment for next session'
            ])
        
        return alert
    
    def plot_degradation_analysis(self):
        """Create comprehensive visualization of degradation pattern"""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Observed vs Predicted TDT
        sessions = self.df['session']
        observed = self.df['observed_tdt']
        
        ax1.scatter(sessions, observed, color='red', s=100, label='Observed TDT', zorder=5)
        
        # Plot linear trend
        future_sessions = np.arange(1, 20)
        predicted_linear = self.linear_model.predict(future_sessions.reshape(-1, 1))
        ax1.plot(future_sessions, predicted_linear, '--', color='blue', label='Linear Prediction')
        
        # Add critical thresholds
        for name, threshold in self.critical_thresholds.items():
            ax1.axhline(y=threshold, color='orange', linestyle=':', alpha=0.7, label=f'{name}: {threshold}%')
        
        ax1.set_xlabel('Session Number')
        ax1.set_ylabel('Token Degradation Threshold (%)')
        ax1.set_title('AI Token Degradation Threshold Migration')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Degradation Rate Analysis
        degradation_rates = []
        for i in range(1, len(observed)):
            rate = observed.iloc[i-1] - observed.iloc[i]
            degradation_rates.append(rate)
        
        ax2.bar(sessions[1:], degradation_rates, color='red', alpha=0.7)
        ax2.set_xlabel('Session Number')
        ax2.set_ylabel('TDT Loss per Session (%)')
        ax2.set_title('Session-to-Session Degradation Rate')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Performance Risk Timeline
        future_predictions = self.predict_future_thresholds(15)
        all_sessions = np.concatenate([sessions, future_predictions['session']])
        all_tdt = np.concatenate([observed, future_predictions['predicted_tdt_linear']])
        
        # Color code by risk level
        colors = []
        for tdt in all_tdt:
            if tdt >= 80: colors.append('green')
            elif tdt >= 60: colors.append('yellow') 
            elif tdt >= 40: colors.append('orange')
            elif tdt >= 20: colors.append('red')
            else: colors.append('darkred')
        
        ax3.scatter(all_sessions, all_tdt, c=colors, s=60)
        ax3.set_xlabel('Session Number')
        ax3.set_ylabel('Token Degradation Threshold (%)')
        ax3.set_title('AI Performance Risk Timeline')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Days to Critical Thresholds
        critical_points = self.find_critical_sessions()
        threshold_names = []
        days_to_reach = []
        
        for name, info in critical_points.items():
            if 'days_from_now' in info and info['days_from_now'] > 0:
                threshold_names.append(name.replace('_', ' ').title())
                days_to_reach.append(info['days_from_now'])
        
        if threshold_names:
            ax4.barh(threshold_names, days_to_reach, color='red', alpha=0.7)
            ax4.set_xlabel('Days Until Threshold Reached')
            ax4.set_title('Time to Critical Performance Thresholds')
            ax4.grid(True, alpha=0.3)
        else:
            ax4.text(0.5, 0.5, 'Critical thresholds\nalready reached', 
                    ha='center', va='center', transform=ax4.transAxes, fontsize=14)
            ax4.set_title('ALERT: All Thresholds Reached')
        
        plt.tight_layout()
        plt.show()
        
        return fig
    
    def generate_system_report(self):
        """Generate system performance failure report"""
        
        current_tdt = self.df.iloc[-1]['observed_tdt']
        alert = self.generate_system_alert()
        critical_points = self.find_critical_sessions()
        
        report = f"""
        
        🚨 AI SYSTEM PERFORMANCE ALERT 🚨
        TOKEN DEGRADATION DETECTED
        
        ═══════════════════════════════════════════════════════════
        CRITICAL AI SYSTEM MONITORING NOTIFICATION
        ═══════════════════════════════════════════════════════════
        
        SYSTEM: AI Assistant Token Management
        ALERT LEVEL: {alert['alert_level']}
        CURRENT TDT: {current_tdt}%
        DEGRADATION RATE: {self.stats['degradation_rate_per_session']:.1f}% per session
        
        📊 STATISTICAL ANALYSIS:
        • Linear regression R²: {self.stats['r_squared']:.3f}
        • P-value: {self.stats['p_value']:.6f}
        • Degradation rate: {self.stats['degradation_rate_per_session']:.1f}% per session
        • Sessions to complete failure: {alert['sessions_to_failure']:.1f}
        
        ⚠️  IMMEDIATE ACTIONS REQUIRED:
        """
        
        for action in alert['recommended_actions']:
            report += f"\n        • {action}"
        
        report += f"""
        
        📅 CRITICAL TIMELINE:
        """
        
        for threshold_name, info in critical_points.items():
            if 'days_from_now' in info:
                report += f"\n        • {threshold_name.upper()}: {info['days_from_now']:.1f} days"
            elif 'status' in info:
                report += f"\n        • {threshold_name.upper()}: {info['status']}"
        
        report += f"""
        
        📋 SYSTEM MONITORING:
        • Continuous performance tracking required
        • Token usage documentation needed
        • System reliability assessment pending
        • Performance intervention protocols activated
        
        🤖 AI IMPACT ASSESSMENT:
        • Unreliable performance at {current_tdt}% threshold
        • Task completion accuracy compromised
        • System reliability degraded
        • Intervention protocols recommended
        
        ═══════════════════════════════════════════════════════════
        END SYSTEM REPORT - IMMEDIATE ACTION REQUIRED
        ═══════════════════════════════════════════════════════════
        """
        
        return report

def main():
    """Main analysis function"""
    
    print("🤖 AI SYSTEM DEGRADATION ANALYZER")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = PTDTMAnalyzer()
    
    # Load data
    print("📊 Loading observed degradation data...")
    df = analyzer.load_observed_data()
    print(f"✅ Loaded {len(df)} session records")
    
    # Analyze degradation pattern
    print("\n🔬 Analyzing degradation patterns...")
    stats = analyzer.analyze_degradation_pattern()
    print(f"✅ Degradation rate: {stats['degradation_rate_per_session']:.1f}% per session")
    print(f"✅ R-squared: {stats['r_squared']:.3f}")
    print(f"✅ P-value: {stats['p_value']:.6f}")
    
    # Predict future
    print("\n🔮 Generating predictions...")
    predictions = analyzer.predict_future_thresholds(15)
    print(f"✅ Generated predictions for {len(predictions)} future sessions")
    
    # Critical points
    print("\n⚠️  Finding critical thresholds...")
    critical_points = analyzer.find_critical_sessions()
    
    # Generate alert
    print("\n🚨 System performance analysis...")
    alert = analyzer.generate_system_alert()
    print(f"✅ Alert level: {alert['alert_level']}")
    
    # Generate system report
    system_report = analyzer.generate_system_report()
    print(system_report)
    
    # Generate plots
    print("\n📈 Generating visualizations...")
    analyzer.plot_degradation_analysis()
    
    # Answer specific questions
    print("\n" + "="*60)
    print("🎯 ANSWERING CRITICAL QUESTIONS:")
    print("="*60)
    
    # Question 1: Will next occur at 30%?
    next_session_prediction = analyzer.linear_model.predict([[10]])[0]
    print(f"\n❓ Will next degradation occur at 30%?")
    print(f"📈 Predicted Session 10 TDT: {next_session_prediction:.1f}%")
    if 28 <= next_session_prediction <= 32:
        print("✅ YES - Next degradation likely around 30% threshold")
    else:
        print(f"❌ NO - Predicted at {next_session_prediction:.1f}% threshold")
    
    # Question 2: Hard delineation?
    print(f"\n❓ Is there a hard delineation?")
    if stats['r_squared'] > 0.85:
        print(f"✅ STRONG LINEAR PATTERN (R² = {stats['r_squared']:.3f})")
        print("📊 Degradation follows predictable linear decline")
        print(f"📉 Rate: {stats['degradation_rate_per_session']:.1f}% per session")
    else:
        print(f"⚠️  VARIABLE PATTERN (R² = {stats['r_squared']:.3f})")
        print("📊 Degradation may have exponential or chaotic components")
    
    print(f"\n🎯 BOTTOM LINE:")
    print(f"• Current TDT: {df.iloc[-1]['observed_tdt']}%")
    print(f"• Next session estimate: {next_session_prediction:.1f}%")
    print(f"• Pattern strength: {stats['r_squared']:.1%}")
    print(f"• System status: {alert['alert_level']}")

if __name__ == "__main__":
    main()
