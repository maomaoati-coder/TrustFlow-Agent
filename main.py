from src.engine import TrustEngine

def main():
    engine = TrustEngine()
    print("\n🛡️ TrustFlow-Agent | Local Verification Engine")
    print("="*45)
    
    # 测试案例：一个成功，一个触发拦截
    test_cases = [
        ("Cloud Sync", "Sync completed: 1024 files uploaded."),
        ("Payment API", "Fatal Error: SSL Certificate Expired.")
    ]
    
    for task, out in test_cases:
        res = engine.run_task(task, out)
        icon = "✅" if res['status'] == "VERIFIED" else "❌"
        print(f"{icon} Task: {task:12} | Status: {res['status']}")
    
    engine.save_audit()
    print("="*45)
    print("📝 Audit report generated: audit_report.json\n")

if __name__ == "__main__":
    main()
