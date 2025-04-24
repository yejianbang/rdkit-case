from rdkit import Chem
from rdkit.Chem import Descriptors

# 创建一个分子
mol = Chem.MolFromSmiles('CCO')

# 计算描述符
mw = Descriptors.MolWt(mol)  # 分子量
logp = Descriptors.MolLogP(mol)  # logP（脂溶性）
num_h_acceptors = Descriptors.NumHAcceptors(mol)  # 氢受体数
num_h_donors = Descriptors.NumHDonors(mol)  # 氢供体数

print(f"Molecular Weight: {mw}")
print(f"logP: {logp}")
print(f"Number of H Acceptors: {num_h_acceptors}")
print(f"Number of H Donors: {num_h_donors}")
