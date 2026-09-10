import hashlib

class SimpleMuSig2:
    """
    MuSig2 Multi-Signature Aggregation Protocol.
    Aggregates public keys and partial Schnorr signatures into a single compact signature.
    """
    def __init__(self, p=10007, g=5):
        self.p = p
        self.g = g

    def keygen(self, privkey):
        return pow(self.g, privkey, self.p)

    def aggregate_pubkeys(self, pub1, pub2):
        return (pub1 * pub2) % self.p

    def compute_signature(self, priv1, r1, priv2, r2, agg_pub, msg):
        R1 = pow(self.g, r1, self.p)
        R2 = pow(self.g, r2, self.p)
        R_agg = (R1 * R2) % self.p
        e = int(hashlib.sha256(f"{R_agg}:{agg_pub}:{msg}".encode()).hexdigest()[:8], 16) % (self.p - 1)
        s1 = (r1 + e * priv1) % (self.p - 1)
        s2 = (r2 + e * priv2) % (self.p - 1)
        s_agg = (s1 + s2) % (self.p - 1)
        return R_agg, s_agg

    def verify(self, agg_pub, msg, R_agg, s_agg):
        e = int(hashlib.sha256(f"{R_agg}:{agg_pub}:{msg}".encode()).hexdigest()[:8], 16) % (self.p - 1)
        lhs = pow(self.g, s_agg, self.p)
        rhs = (R_agg * pow(agg_pub, e, self.p)) % self.p
        return lhs == rhs
