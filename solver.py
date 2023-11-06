from ortools.linear_solver import pywraplp

def _or_1():
    # Crear un solver de programación lineal
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Definir variables
    X1 = solver.NumVar(0, solver.infinity(), 'x1')
    X2 = solver.NumVar(0, solver.infinity(), 'x2')


    # Definir función objetivo
    solver.Maximize(2*X1 + X2)

    # Definir restricciones
    solver.Add(X1 + X2 <= 8)
    solver.Add(3*X1 + X2 <= 18)
    
    # Resolver el problema
    solver.Solve()

    # Obtener los valores óptimos de las variables
    optimal_X1 = X1.solution_value()
    optimal_X2 = X2.solution_value()
    optimal_Z = solver.Objective().Value()
    return optimal_X1 ,optimal_X2 ,optimal_Z

def _or_2():
    # Crear un solver de programación lineal
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Definir variables
    X1 = solver.NumVar(-solver.infinity(), 0, 'x1')
    X2 = solver.NumVar(0, solver.infinity(), 'x2')


    # Definir función objetivo
    solver.Maximize(2*X1 + X2)

    # Definir restricciones
    solver.Add(-X1 + X2 <= 8)
    solver.Add(-3*X1 + X2 <= 18)
    
    # Resolver el problema
    solver.Solve()

    # Obtener los valores óptimos de las variables
    optimal_X1 = X1.solution_value()
    optimal_X2 = X2.solution_value()
    optimal_Z = solver.Objective().Value()
    return optimal_X1 ,optimal_X2 ,optimal_Z

def _or_3():
    # Crear un solver de programación lineal
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Definir variables
    X1 = solver.NumVar(-solver.infinity(), 0, 'x1')
    X2 = solver.NumVar(-solver.infinity(), 0, 'x2')


    # Definir función objetivo
    solver.Maximize(2*X1 + X2)

    # Definir restricciones
    solver.Add(-X1 - X2 <= 8)
    solver.Add(-3*X1 - X2 <= 18)
    
    # Resolver el problema
    solver.Solve()

    # Obtener los valores óptimos de las variables
    optimal_X1 = X1.solution_value()
    optimal_X2 = X2.solution_value()
    optimal_Z = solver.Objective().Value()
    return optimal_X1 ,optimal_X2 ,optimal_Z

def _or_4():
    # Crear un solver de programación lineal
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Definir variables
    X1 = solver.NumVar(0, solver.infinity(), 'x1')
    X2 = solver.NumVar(-solver.infinity(), 0, 'x2')


    # Definir función objetivo
    solver.Maximize(2*X1 + X2)

    # Definir restricciones
    solver.Add(X1 - X2 <= 8)
    solver.Add(3*X1 - X2 <= 18)
    
    # Resolver el problema
    solver.Solve()

    # Obtener los valores óptimos de las variables
    optimal_X1 = X1.solution_value()
    optimal_X2 = X2.solution_value()
    optimal_Z = solver.Objective().Value()
    return optimal_X1 ,optimal_X2 ,optimal_Z

def main():
    cuadrante = input("Que cuadrante deseas optimizar? (1,2,3,4): ")
    if cuadrante == '1':
        optimal_X1 ,optimal_X2 ,optimal_Z = _or_1()
    elif cuadrante == '2':
        optimal_X1 ,optimal_X2 ,optimal_Z = _or_2()
    elif cuadrante == '3':
        optimal_X1 ,optimal_X2 ,optimal_Z = _or_3()
    elif cuadrante == '4':
        optimal_X1 ,optimal_X2 ,optimal_Z = _or_4()
    else:
        print('No se ha seleccionado un cuadrante valido')
    if optimal_X1 == 0 and optimal_X2 == 0:
        print('No se ha encontrado solucion')
    else:
        
        print('X1 =', round(optimal_X1,0))
        print('X2 =', round(optimal_X2,0))
        print('Z =', round(optimal_Z,0))


if __name__=='__main__':
    main()