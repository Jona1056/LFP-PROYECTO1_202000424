
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DECIMAL DIV ENTERO IGUAL LLAA LLAC RCOSENO RDIVISION RINVERSO RMOD RMULTIPLICACION RNUMERO ROPERACION RPOTENCIA RRAIZ RRESTA RSENO RSUMA RTANGENTE RTIPOinit : instruccionesinstrucciones    : instrucciones instruccion\n                        |   instruccioninstruccion  : LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLACinstrucciones_2 : instrucciones_2 instruccion_2instrucciones_2 :  instruccion_2instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLACinstruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC tipo :   RSUMA\n            |   RRESTA\n            |   RMULTIPLICACION\n            |   RDIVISION\n            |   RPOTENCIA\n            |   RRAIZ\n            |   RINVERSO\n            |   RSENO\n            |   RCOSENO\n            |   RTANGENTE\n            |   RMOD\n    '
    
_lr_action_items = {'LLAA':([0,2,3,5,7,9,10,14,30,31,33,36,37,44,45,47,],[4,4,-3,-2,8,13,-6,-5,34,35,8,-4,40,-8,-9,-7,]),'$end':([1,2,3,5,36,],[0,-1,-3,-2,-4,]),'RTIPO':([4,17,],[6,32,]),'LLAC':([6,12,18,19,20,21,22,23,24,25,26,27,28,29,32,41,42,46,],[7,16,33,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,36,44,45,47,]),'ROPERACION':([8,13,40,43,],[11,11,11,46,]),'RNUMERO':([8,13,38,39,40,],[12,12,41,42,12,]),'IGUAL':([11,],[15,]),'DIV':([13,34,35,40,],[17,38,39,43,]),'RSUMA':([15,],[19,]),'RRESTA':([15,],[20,]),'RMULTIPLICACION':([15,],[21,]),'RDIVISION':([15,],[22,]),'RPOTENCIA':([15,],[23,]),'RRAIZ':([15,],[24,]),'RINVERSO':([15,],[25,]),'RSENO':([15,],[26,]),'RCOSENO':([15,],[27,]),'RTANGENTE':([15,],[28,]),'RMOD':([15,],[29,]),'DECIMAL':([16,],[30,]),'ENTERO':([16,],[31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,5,]),'instrucciones_2':([7,33,],[9,37,]),'instruccion_2':([7,9,33,37,],[10,14,10,14,]),'tipo':([15,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','numeros.py',115),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','numeros.py',120),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','numeros.py',121),
  ('instruccion -> LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC','instruccion',8,'p_instruccion','numeros.py',129),
  ('instrucciones_2 -> instrucciones_2 instruccion_2','instrucciones_2',2,'p_instrucciones_2_lista','numeros.py',133),
  ('instrucciones_2 -> instruccion_2','instrucciones_2',1,'p_instrucciones_2_instruccion','numeros.py',138),
  ('instruccion_2 -> LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC','instruccion_2',10,'p_instruccion_2','numeros.py',143),
  ('instruccion_2 -> LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_decimal','numeros.py',150),
  ('instruccion_2 -> LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_entero','numeros.py',154),
  ('tipo -> RSUMA','tipo',1,'p_tipo','numeros.py',165),
  ('tipo -> RRESTA','tipo',1,'p_tipo','numeros.py',166),
  ('tipo -> RMULTIPLICACION','tipo',1,'p_tipo','numeros.py',167),
  ('tipo -> RDIVISION','tipo',1,'p_tipo','numeros.py',168),
  ('tipo -> RPOTENCIA','tipo',1,'p_tipo','numeros.py',169),
  ('tipo -> RRAIZ','tipo',1,'p_tipo','numeros.py',170),
  ('tipo -> RINVERSO','tipo',1,'p_tipo','numeros.py',171),
  ('tipo -> RSENO','tipo',1,'p_tipo','numeros.py',172),
  ('tipo -> RCOSENO','tipo',1,'p_tipo','numeros.py',173),
  ('tipo -> RTANGENTE','tipo',1,'p_tipo','numeros.py',174),
  ('tipo -> RMOD','tipo',1,'p_tipo','numeros.py',175),
]
