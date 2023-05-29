# %%
def comprobar(a): #Función utilizada para eliminar filas de la bd
    return a.shape, a.columns, a.isna().sum()

# %%
