from rdkit import Chem

# 定义分子
mol = Chem.MolFromSmiles('C[C@@H](O)[C@H](O)C')  # 指定手性中心

# 移除立体化学信息
Chem.RemoveStereochemistry(mol)

# 输出结果
print("Molecule without stereochemistry:", Chem.MolToSmiles(mol))
