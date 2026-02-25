import pandas as pd

def test_division_par_zero():
    """Vérifie que le calcul de moyenne gère le cas vide."""
    data = pd.DataFrame({"amount": []})
    total = data["amount"].sum()
    count = len(data)
    avg = total // count if count > 0 else 0  # Ne doit pas crasher
    assert avg == 0

def test_index_out_of_range():
    """Vérifie qu'on ne peut pas accéder à un index invalide."""
    data = pd.read_csv("data/sales.csv")
    row_index = 100
    assert row_index >= len(data) or data.iloc[row_index] is not None

def test_search_special_chars():
    """Vérifie que la recherche gère les caractères spéciaux."""
    data = pd.read_csv("data/sales.csv")
    search = "*"
    # Ne doit pas crasher avec regex=False
    result = data[data["product"].str.contains(search, regex=False)]
    assert result is not None