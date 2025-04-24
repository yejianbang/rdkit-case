from rdkit import Chem
from rdkit.Chem import AllChem

# 定义反应
reaction = AllChem.ReactionFromSmarts('[OH:1][C:2]>>[O:1]=[C:2]')  # 乙醇氧化为乙醛

# 定义反应物
reactant = Chem.MolFromSmiles('CCO')  # Ethanol

# 运行反应
products = reaction.RunReactants((reactant,))

# 输出反应产物
for product_set in products:
    for product in product_set:
        print(Chem.MolToSmiles(product))
