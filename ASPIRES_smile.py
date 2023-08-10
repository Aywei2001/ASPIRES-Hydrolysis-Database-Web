import pandas as pd
# from rdkit import Chem
from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

app = Flask(__name__, static_folder='templates')
CORS(app, origins='http://localhost:8000')


# search is utilized to find SMILE

# linear search test
#may not be used in the future, use for looking for SMILE that user inputed
def linear_smile(smile_frame, smile):
    for item in smile_frame:
        if item == smile:
            return smile
    return None



def get_reactant_opt(search_smile, find_hydro):
    #original code

    #idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    idx = find_hydro.loc[find_hydro["reactant_smiles"] == search_smile].index
    print(idx) #test to print index
    df_idx = find_hydro.loc[idx] #df_idx stores the index in order to match the index to value being serached for
    print(df_idx['reactant_opt_energy']) #test to print value

    #looping code test to see if
    for index in idx:
        reactant_opt_energy = find_hydro.loc[index, 'reactant_opt_energy']
        print(f"Index: {index}, Reactant Opt Energy: {reactant_opt_energy}") #

    reactant_opt_energy_values = df_idx['reactant_opt_energy'].tolist() #return value to main
    return reactant_opt_energy_values


def get_reactant_sp(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx) #test to print index

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['reactant_sp_energy'])#test to print value

    reactant_sp_values = df_idx["reactant_sp_energy"].tolist() #return value to main
    return reactant_sp_values


def get_enthalpy(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['reactant_enthalpy'])#test to print value

    reactant_enthalpy = df_idx["reactant_enthalpy"].tolist()#return value to main
    return reactant_enthalpy


def get_entropy(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['reactant_entropy'])#test to print value

    reactant_entropy = df_idx["reactant_entropy"].tolist()#return value to main
    return reactant_entropy


def get_product_smiles(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index in terminal

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['product_smiles'])#test to print value in terminal

    product_smiles = df_idx["product_smiles"].tolist()#return value to main
    return product_smiles


def get_functional_group(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index in terminal

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['functional_group_reacted'])#test to print value in terminal




def get_product_opt(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index in terminal

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['product_opt_energy'])#test to print value in terminal

    product_opt_energy = df_idx["product_opt_energy"].tolist()
    return product_opt_energy

def get_product_sp(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)#test to print index in terminal

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['product_sp_energy'])#test to print value in terminal

    product_sp_energy = df_idx["product_sp_energy"].tolist()
    return product_sp_energy


def get_product_enthalpy(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]#df_idx stores the index in order to match the index to value being serached for
    print(df_idx['product_enthalpy'])

    product_enthalpy = df_idx["product_enthalpy"].tolist()
    return product_enthalpy


def get_product_entropy(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['product_entropy'])

    product_entropy = df_idx["product_entropy"].tolist()
    return product_entropy


def get_dE_opt(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dE_opt'])

    get_dE_opt = df_idx["dE_opt"].tolist()
    return get_dE_opt


def get_dE_sp(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dE_sp'])

    get_dE_sp = df_idx["dE_sp"].tolist()
    return get_dE_sp

def get_dH(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dH'])

    get_dH = df_idx["dH"].tolist()
    return get_dH

def get_dS(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dS'])

    get_dS = df_idx["dS"].tolist()
    return get_dS

def get_dG_opt(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dG_opt'])

    get_dG_opt = df_idx["dG_opt"].tolist()
    return get_dG_opt

def get_dG_sp(search_smile, find_hydro):
    idx = find_hydro.index[find_hydro["reactant_smiles"] == search_smile]
    print(idx)

    df_idx = find_hydro.loc[idx]
    print(df_idx['dG_sp'])

    get_dG_sp = df_idx["dG_sp"].tolist()
    return get_dG_sp


@app.route('/', methods=['GET'])
def index():
    welcome_message = "Welcome to the Flask server!"
    return welcome_message + render_template('ASPIRES_web.html')


@app.route('/hello', methods=['GET']) #Welcome message is to be displayed as
def hello():
    message = "Welcome!"
    response = {'message': message}
    return jsonify(response)

#database is read from a json file into a dataframe
hydro_df = pd.read_json('Hydrolysis_reactions_for_UI_creation_ASPIRES.json')


@app.route('/main', methods=['POST'])
def main():
    #reactant_smiles column is read out from the the dataframe into list
    list_smiles = hydro_df.loc[:, "reactant_smiles"]
    get_smiles = []

    #
    i = 0
    while i < len(list_smiles):
        smiles = hydro_df.reactant_smiles.iloc[i]
        get_smiles.append(smiles)
        i += 1

    search_smiles = request.form.get('smile')
    if request.method == "POST": #make POST request to
        search_smiles = request.form['smile']

        #
        result_smile = linear_smile(get_smiles, search_smiles)

        #
        # result_smile = hydro_df[hydro_df["reactant_smiles"].str.contains(search_smiles, regex=False)]

    # if SMILE is found, display SMILE
    if result_smile is not None:
        # found_smiles = result_smile['reactant_smiles'].tolist()

        #found SMILE is stored here
        found_smiles = result_smile
        #matching values are returned here from their individual search functions and stored in variables
        reactant_opt_energy_values = get_reactant_opt(search_smiles, hydro_df)
        reactant_sp_values = get_reactant_sp(search_smiles, hydro_df)
        enthalpy_value = get_enthalpy(search_smiles, hydro_df)
        entropy_value = get_entropy(search_smiles, hydro_df)
        product_smile = get_product_smiles(search_smiles, hydro_df)
        product_opt_energy = get_product_opt(search_smiles, hydro_df)
        product_sp_energy = get_product_sp(search_smiles, hydro_df)
        product_enthalpy = get_product_enthalpy(search_smiles, hydro_df)
        product_entropy = get_product_entropy(search_smiles, hydro_df)
        dE_opt_value = get_dE_opt(search_smiles, hydro_df),
        dE_sp_value = get_dE_sp(search_smiles, hydro_df),
        dH_value = get_dH(search_smiles, hydro_df),
        dS_value = get_dS(search_smiles, hydro_df),
        dG_opt_value = get_dG_opt(search_smiles, hydro_df),
        dG_sp_value = get_dG_sp(search_smiles, hydro_df)


        response = {
            'message': 'Found SMILE',
            'result': found_smiles,
            'properties':{
                #values contained in
                'reactant_opt_energy': reactant_opt_energy_values,
                'reactant_sp_energy': reactant_sp_values,
                'reactant_enthalpy': enthalpy_value,
                'reactant_entropy': entropy_value,
                'product_smile': product_smile,
                'product_opt_energy': product_opt_energy,
                'product_sp_energy': product_sp_energy,
                'product_enthalpy': product_enthalpy,
                'product_entropy': product_entropy,
                'de_opt': dE_opt_value,
                'de_sp': dE_sp_value,
                'dh': dH_value,
                'ds': dS_value,
                'dg_opt': dG_opt_value,
                'dg_sp': dG_sp_value,
            }
        }
    # if SMILE is not found, print out "SMILE not found"
    else:
        #response message delivered to front end
        response = {
            'message': 'SMILE not available',
            'result': []
        }

    flask_response = make_response(jsonify(response))
    flask_response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    flask_response.headers['Pragma'] = 'no-cache'
    flask_response.headers['Expires'] = '0'

    return flask_response


if __name__ == '__main__':
    # main()
    app.run(port=5000)