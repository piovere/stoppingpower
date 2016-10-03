from pyne import data
from pyne import nuc_data
from pyne.material import MaterialLibrary


mats = MaterialLibrary(nuc_data, datapath='/material_library/materials', nucpath='/material_library/nucid')
