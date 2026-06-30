import ast, os, json
import plugins.secrets

def run_auditor():
    report = []
    for filename in os.listdir("."):
        if filename.endswith(".py") and filename != "forge_engine.py":
            with open(filename, "r") as f:
                tree = ast.parse(f.read())
            
            # Run the plugin
            hardener = plugins.secrets.SecretsDetector()
            new_tree = hardener.visit(tree)
            ast.fix_missing_locations(new_tree)
            
            # Save the hardened code
            with open(f"hardened_{filename}", "w") as f:
                f.write(ast.unparse(new_tree))
                
            report.append({"file": filename, "status": "Hardened"})
    
    # Save professional report
    with open("audit_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\n[+] Audit Complete. Check 'audit_report.json' and 'hardened_vulnerable_code.py'")

if __name__ == "__main__":
    run_auditor()