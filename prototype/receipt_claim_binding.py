"""Prototype pédagogique : lier un reçu RISC Zero à son claim public."""

def claim_digest(claim):
    fields=(claim.get("journal_digest"),claim.get("image_id"),claim.get("exit_code"))
    return hash(fields) if all(x is not None for x in fields) else None

def receipt_matches(receipt, claim):
    return (isinstance(receipt,dict) and isinstance(claim,dict)
            and receipt.get("claim_digest")==claim_digest(claim)
            and receipt.get("seal") is not None)

if __name__ == "__main__":
    c={"journal_digest":"j","image_id":"img","exit_code":0}
    r={"claim_digest":claim_digest(c),"seal":"s"}
    assert receipt_matches(r,c)
    assert not receipt_matches({**r,"claim_digest":0},c)
