from rdkit import Chem

# 定义分子
mol = Chem.MolFromSmiles('CC(=O)OCC')  # Ethyl acetate

# 手动分解分子（断开特定键）
bonds_to_break = [1]  # 指定键索引（例如，第 1 个键）
fragments = Chem.FragmentOnBonds(mol, bonds_to_break)

# 输出分解后的分子片段
print(Chem.MolToSmiles(fragments))
