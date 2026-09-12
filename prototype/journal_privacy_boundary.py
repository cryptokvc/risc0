"""Prototype pédagogique : séparer données privées et sortie publique du journal."""

PUBLIC_FIELDS=("result_digest","version")

def public_journal(journal):
    if not isinstance(journal,dict) or any(journal.get(k) is None for k in PUBLIC_FIELDS):
        return None
    return {k:journal[k] for k in PUBLIC_FIELDS}

def public_output_is_stable(before, after):
    return public_journal(before) is not None and public_journal(before)==public_journal(after)

if __name__ == "__main__":
    a={"result_digest":"d","version":1,"secret":"hidden"}
    b={"result_digest":"d","version":1,"secret":"other"}
    assert public_output_is_stable(a,b)
    assert public_journal(a)=={"result_digest":"d","version":1}
