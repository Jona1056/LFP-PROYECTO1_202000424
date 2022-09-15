
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DECIMAL DIV ENTERO IGUAL LLAA LLAC RDIVISION RMULTIPLICACION RNUMERO ROPERACION RPOTENCIA RRAIZ RRESTA RSUMA RTIPOinit : instruccionesinstrucciones    : instrucciones instruccion\n                        |   instruccioninstruccion  : LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLACinstrucciones_2 : instrucciones_2 instruccion_2instrucciones_2 :  instruccion_2instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLACinstruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC tipo :   RSUMA\n            |   RRESTA\n            |   RMULTIPLICACION\n            |   RDIVISION\n            |   RPOTENCIA\n            |   RRAIZ\n    '
    
_lr_action_items = {'LLAA':([0,2,3,5,7,9,10,14,25,26,28,31,32,39,40,42,],[4,4,-3,-2,8,13,-6,-5,29,30,8,-4,35,-8,-9,-7,]),'$end':([1,2,3,5,31,],[0,-1,-3,-2,-4,]),'RTIPO':([4,17,],[6,27,]),'LLAC':([6,12,18,19,20,21,22,23,24,27,36,37,41,],[7,16,28,-10,-11,-12,-13,-14,-15,31,39,40,42,]),'ROPERACION':([8,13,35,38,],[11,11,11,41,]),'RNUMERO':([8,13,33,34,35,],[12,12,36,37,12,]),'IGUAL':([11,],[15,]),'DIV':([13,29,30,35,],[17,33,34,38,]),'RSUMA':([15,],[19,]),'RRESTA':([15,],[20,]),'RMULTIPLICACION':([15,],[21,]),'RDIVISION':([15,],[22,]),'RPOTENCIA':([15,],[23,]),'RRAIZ':([15,],[24,]),'DECIMAL':([16,],[25,]),'ENTERO':([16,],[26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,5,]),'instrucciones_2':([7,28,],[9,32,]),'instruccion_2':([7,9,28,32,],[10,14,10,14,]),'tipo':([15,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','numeros.py',105),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','numeros.py',110),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','numeros.py',111),
  ('instruccion -> LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC','instruccion',8,'p_instruccion','numeros.py',119),
  ('instrucciones_2 -> instrucciones_2 instruccion_2','instrucciones_2',2,'p_instrucciones_2_lista','numeros.py',123),
  ('instrucciones_2 -> instruccion_2','instrucciones_2',1,'p_instrucciones_2_instruccion','numeros.py',129),
  ('instruccion_2 -> LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC','instruccion_2',10,'p_instruccion_2','numeros.py',134),
  ('instruccion_2 -> LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_decimal','numeros.py',138),
  ('instruccion_2 -> LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_entero','numeros.py',142),
  ('tipo -> RSUMA','tipo',1,'p_tipo','numeros.py',153),
  ('tipo -> RRESTA','tipo',1,'p_tipo','numeros.py',154),
  ('tipo -> RMULTIPLICACION','tipo',1,'p_tipo','numeros.py',155),
  ('tipo -> RDIVISION','tipo',1,'p_tipo','numeros.py',156),
  ('tipo -> RPOTENCIA','tipo',1,'p_tipo','numeros.py',157),
  ('tipo -> RRAIZ','tipo',1,'p_tipo','numeros.py',158),
]