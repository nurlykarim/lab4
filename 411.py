import sys
import json

source = json.loads(sys.stdin.readline())
patch = json.loads(sys.stdin.readline())

def apply_patch(src, p):
  
    if isinstance(src, dict) and isinstance(p, dict):
        result = dict(src)
        for k, v in p.items():
            if v is None:
                result.pop(k, None)  # remove key
            elif k in result:
                result[k] = apply_patch(result[k], v)
            else:
                result[k] = v
        return result
  
    return p

result = apply_patch(source, patch)

print(json.dumps(result, separators=(',', ':'), sort_keys=True))