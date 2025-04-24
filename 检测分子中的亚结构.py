from rdkit import Chem

# 定义目标分子和子结构
mol = Chem.MolFromSmiles('CCOC')  # Ethyl methyl ether
substruct = Chem.MolFromSmiles('CO')  # Substructure: Alcohol group

# 检测子结构是否存在
if mol.HasSubstructMatch(substruct):
    print("Substructure match found!")
else:
    print("No match found.")
