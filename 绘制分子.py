from rdkit import Chem
from rdkit.Chem import Draw

# 创建一个分子
mol = Chem.MolFromSmiles('CCO')  # Ethanol

# 保存分子图片到文件
Draw.MolToFile(mol, 'molecule.png')
print("Molecule image saved as molecule.png")
