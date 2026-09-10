from client import SimpleMuSig2
import json

def handle_request(req):
    musig = SimpleMuSig2()
    action = req.get("action")
    if action == "verify":
        agg_pub = req.get("agg_pub", 0)
        msg = req.get("msg", "")
        R_agg = req.get("R_agg", 0)
        s_agg = req.get("s_agg", 0)
        return {"status": "ok", "valid": musig.verify(agg_pub, msg, R_agg, s_agg)}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "verify"})))
