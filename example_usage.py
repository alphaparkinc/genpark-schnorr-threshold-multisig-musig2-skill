from client import SimpleMuSig2

def main():
    print("=== Testing MuSig2 Multi-Signature Scheme ===")
    musig = SimpleMuSig2()
    
    priv1, priv2 = 23, 47
    pub1 = musig.keygen(priv1)
    pub2 = musig.keygen(priv2)
    agg_pub = musig.aggregate_pubkeys(pub1, pub2)
    
    msg = "authorize_transfer_100_tokens"
    R_agg, s_agg = musig.compute_signature(priv1, 13, priv2, 17, agg_pub, msg)
    print(f"Aggregated Pubkey: {agg_pub}")
    print(f"Aggregated Signature (R, s): ({R_agg}, {s_agg})")
    
    valid = musig.verify(agg_pub, msg, R_agg, s_agg)
    print(f"Signature Verification: {valid}")
    assert valid
    
    invalid = musig.verify(agg_pub, "tampered_msg", R_agg, s_agg)
    print(f"Tampered Verification (should be False): {invalid}")
    assert not invalid
    print("=== MuSig2 Verification Complete ===")

if __name__ == "__main__":
    main()
