"""Prototype pédagogique : vérifier l'identité du guest avant d'accepter un reçu."""

def method_is_expected(receipt, expected_ids):
    return (isinstance(receipt,dict) and isinstance(receipt.get("method_id"),str)
            and receipt["method_id"] in set(expected_ids))

def accept_guest(receipt, expected_ids, expected_exit=0):
    return method_is_expected(receipt,expected_ids) and receipt.get("exit_code")==expected_exit

if __name__ == "__main__":
    r={"method_id":"m1","exit_code":0}
    assert accept_guest(r,["m1"])
    assert not accept_guest({**r,"method_id":"m2"},["m1"])
    assert not accept_guest({**r,"exit_code":1},["m1"])
