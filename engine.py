import json
from datetime import datetime

class TrustEngine:
    def __init__(self):
        self.audit_log = []

    def validate(self, output):
        """标准验证节点：检测幻觉和错误关键字"""
        failure_keywords = ["error", "failed", "timeout", "invalid", "exception", "refused"]
        output_str = str(output).lower()
        for word in failure_keywords:
            if word in output_str:
                return False
        return True

    def run_task(self, task_name, mock_output):
        """执行任务并记录审计追踪"""
        verified = self.validate(mock_output)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task_name,
            "raw_output": mock_output,
            "status": "VERIFIED" if verified else "BLOCKED"
        }
        self.audit_log.append(entry)
        return entry

    def save_audit(self, filename="audit_report.json"):
        with open(filename, "w") as f:
            json.dump(self.audit_log, f, indent=4)
