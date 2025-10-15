# %%
# Cargue los datos de la tabla "files/input/drivers.csv" a una variable llamada `drivers`, usando pandas.
import pandas as pd
drivers = pd.read_csv("../files/input/drivers.csv")

# %%
# Cargue los datos de la tabla "files/input/timesheet.csv" a una variable llamada `timesheet`, usando pandas.
timesheet = pd.read_csv("../files/input/timesheet.csv")

# %%
# Calcule el promedio de las columnas "hours-logged" y "miles-logged" en la tabla "timesheet", agrupando los resultados por cada conductor (driverId).
average_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].mean().reset_index()
average_timesheet

# %%
# Cree una tabla llamada "timesheet_with_means" basada en la tabla "timesheet", agregando una columna con el promedio de "hours-logged" para cada conductor (driverId).
timesheet_with_means = timesheet.merge(average_timesheet[["driverId", "hours-logged"]], on="driverId", suffixes=("", "_mean"))

# %%
