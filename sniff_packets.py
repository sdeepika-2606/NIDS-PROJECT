from scapy.all import sniff
import pandas as pd

data = []

def get_features(pkt):
    try:
        data.append({
            'protocol_type': pkt.proto if hasattr(pkt, 'proto') else 0,
            'src_bytes': len(pkt),
            'dst_bytes': 0  # Can’t extract everything without deep parsing
        })
    except:
        pass

sniff(count=10, prn=get_features)

df = pd.DataFrame(data)
df.to_csv("scapy_live_packets.csv", index=False)
print("✅ Saved as scapy_live_packets.csv")
