import inspect
from IPython.display import HTML
from files import *
from random import randint
from copy import deepcopy


def tester_file_2(f):
    a_tester = []
    a_tester.append([[],8])
    a_tester.append([[8],8])
    a_tester.append([[7],8])
    a_tester.append([[0,6,8],9])
    a_tester.append([[0,6,8],0])
    a_tester.append([[0,6,8],8])
    a_tester.append([[0,8,8],8])
    a_tester.append([[8,8,8],8])
    for i in range(8):
        t = [randint(1,10) for j in range(5)]
        x = randint(1,10)
        a_tester.append([t,x])
    return test(f,a_tester)

def tester_file(f):
    a_tester = []
    a_tester.append([8])
    a_tester.append([1,5])
    a_tester.append([5,1])
    a_tester.append([0])
    a_tester.append([-7])
    a_tester.append([-7,7])
    a_tester.append([7,-7])
    for i in range(8):
        t = [randint(-10,10) for j in range(8)]  # puissance de 2 pour la moyenne
        a_tester.append(t)
    return test(f,a_tester)
    
def compter_correction(f,c):
    return f.count(c)

def maximum_correction(f):
    #assert len(f)>0, "la liste ne doit pas être vide !"
    return max(f)

def moyenne_correction(f):
    #assert len(f)>0, "la liste ne doit pas être vide !"
    return sum(f)/len(f)
    

def test(candidate, values, test_type=False):
    redcross = '&#10060;'
    checked = '&#9989;'
    
    # get _correction function
    fonction = candidate.__name__
    good=globals()[fonction+"_correction"]
    # check parametres
    sgood = inspect.signature(good)
    nbParamGood = len(sgood.parameters)
    scand = inspect.signature(candidate)
    nbParamCandidate = len(scand.parameters)
    if nbParamGood != nbParamCandidate:
        return("Erreur ! Votre fonction attend {nbc} variables au lieu de {nbg}".format(nbg=nbParamGood, nbc=nbParamCandidate))

    # Build table
    code = """<table><thead><tr>
          <th>{param}</th>
          <th>{f}{param}<br/> attendu</th>
          <th>{f}{param}<br/> calculé</th>
          <th>Test</th>
        </tr></thead><tbody>""".format(f=fonction, param=scand)

    # Test return values from function and function_correction
    # Build row
    row = """<tr style='background-color:{color}'>
          <td> {x} </td>
          <td> {good} </td>
          <td><b>{candidate}</b></td>
          <td> {check}</td></td>"""
          
    for x in values:
        y = deepcopy(x)
        if nbParamGood > 1:
            result = candidate(*x)
            solution = good(*y)
        else:
            result = candidate(x)
            solution = good(y)
        if solution is result if test_type else solution == result:
             color, check = '#beffb5', checked
        else:
             color, check = '#ffb5b5', redcross
        code = code+row.format(x=y, good=solution, candidate=result, color=color, check=check) 
          
          
    # Closing html tags
    code = code+"""</tbody></table>"""
    return(HTML(code))      