from rdkit import Chem
from rdkit.Chem import AllChem

# 定义分子
mol = Chem.MolFromSmiles('CCO')

# 生成 2D 坐标
AllChem.Compute2DCoords(mol)

# 打印 2D 坐标
for atom in mol.GetAtoms():
    pos = mol.GetConformer().GetAtomPosition(atom.GetIdx())
    print(f"Atom {atom.GetSymbol()}: x={pos.x}, y={pos.y}")
