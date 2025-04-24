from rdkit import DataStructs
from rdkit.Chem import MolFromSmiles
from rdkit.Chem import AllChem, rdMolDescriptors

# 创建两个分子对象
m1 = MolFromSmiles('CCO')  # Ethanol
m2 = MolFromSmiles('CCN')  # Ethylamine

# 计算 MACCS keys
f1 = rdMolDescriptors.GetMACCSKeysFingerprint(m1)
f2 = rdMolDescriptors.GetMACCSKeysFingerprint(m2)

# 比较两个分子的相似度（Tanimoto 系数）
similarity = DataStructs.FingerprintSimilarity(f1, f2)
print("Tanimoto similarity between m1 and m2:", similarity)
