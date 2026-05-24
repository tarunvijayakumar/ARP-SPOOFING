from scapy.all import sniff, ARP
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

model = joblib.load('arp_model.pkl')

def extract_features(pkt):
    return [pkt[ARP].hwsrc, pkt[ARP].psrc, len(pkt)]

def detect_arp_ml(pkt):
    if pkt.haslayer(ARP):
        features = extract_features(pkt)
        prediction = model.predict([features])
        if prediction == 1:
            print("ALERT: ARP spoofing detected!")

if __name__ == "__main__":
    sniff(filter="arp", prn=detect_arp_ml, store=0)
