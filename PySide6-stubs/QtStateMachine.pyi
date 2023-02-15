# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtStateMachine, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtStateMachine`

import PySide6.QtStateMachine
import PySide6.QtCore
import PySide6.QtGui

from typing import Any, Optional, Type, Union, Sequence, List, Set, overload


class QAbstractState(PySide6.QtCore.QObject):

    def __init__(self, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def active(self) -> bool: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def machine(self) -> PySide6.QtStateMachine.QStateMachine: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None: ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None: ...
    def parentState(self) -> PySide6.QtStateMachine.QState: ...


class QAbstractTransition(PySide6.QtCore.QObject):

    class TransitionType(shibokensupport.enum_310.Enum):

        ExternalTransition       : QAbstractTransition.TransitionType = ... # 0x0
        InternalTransition       : QAbstractTransition.TransitionType = ... # 0x1


    def __init__(self, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def addAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None: ...
    def animations(self) -> List[PySide6.QtCore.QAbstractAnimation]: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def machine(self) -> PySide6.QtStateMachine.QStateMachine: ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None: ...
    def removeAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None: ...
    def setTargetState(self, target: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def setTargetStates(self, targets: Sequence[PySide6.QtStateMachine.QAbstractState]) -> None: ...
    def setTransitionType(self, type: PySide6.QtStateMachine.QAbstractTransition.TransitionType) -> None: ...
    def sourceState(self) -> PySide6.QtStateMachine.QState: ...
    def targetState(self) -> PySide6.QtStateMachine.QAbstractState: ...
    def targetStates(self) -> List[PySide6.QtStateMachine.QAbstractState]: ...
    def transitionType(self) -> PySide6.QtStateMachine.QAbstractTransition.TransitionType: ...


class QEventTransition(PySide6.QtStateMachine.QAbstractTransition):

    @overload
    def __init__(self, object: PySide6.QtCore.QObject, type: PySide6.QtCore.QEvent.Type, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def eventSource(self) -> PySide6.QtCore.QObject: ...
    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def eventType(self) -> PySide6.QtCore.QEvent.Type: ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None: ...
    def setEventSource(self, object: PySide6.QtCore.QObject) -> None: ...
    def setEventType(self, type: PySide6.QtCore.QEvent.Type) -> None: ...


class QFinalState(PySide6.QtStateMachine.QAbstractState):

    def __init__(self, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None: ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None: ...


class QHistoryState(PySide6.QtStateMachine.QAbstractState):

    class HistoryType(shibokensupport.enum_310.Enum):

        ShallowHistory           : QHistoryState.HistoryType = ... # 0x0
        DeepHistory              : QHistoryState.HistoryType = ... # 0x1


    @overload
    def __init__(self, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, type: PySide6.QtStateMachine.QHistoryState.HistoryType, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def defaultState(self) -> PySide6.QtStateMachine.QAbstractState: ...
    def defaultTransition(self) -> PySide6.QtStateMachine.QAbstractTransition: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def historyType(self) -> PySide6.QtStateMachine.QHistoryState.HistoryType: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None: ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None: ...
    def setDefaultState(self, state: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def setDefaultTransition(self, transition: PySide6.QtStateMachine.QAbstractTransition) -> None: ...
    def setHistoryType(self, type: PySide6.QtStateMachine.QHistoryState.HistoryType) -> None: ...


class QIntList(object): ...


class QKeyEventTransition(PySide6.QtStateMachine.QEventTransition):

    @overload
    def __init__(self, object: PySide6.QtCore.QObject, type: PySide6.QtCore.QEvent.Type, key: int, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def key(self) -> int: ...
    def modifierMask(self) -> PySide6.QtCore.Qt.KeyboardModifier: ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None: ...
    def setKey(self, key: int) -> None: ...
    def setModifierMask(self, modifiers: PySide6.QtCore.Qt.KeyboardModifier) -> None: ...


class QMouseEventTransition(PySide6.QtStateMachine.QEventTransition):

    @overload
    def __init__(self, object: PySide6.QtCore.QObject, type: PySide6.QtCore.QEvent.Type, button: PySide6.QtCore.Qt.MouseButton, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def button(self) -> PySide6.QtCore.Qt.MouseButton: ...
    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def hitTestPath(self) -> PySide6.QtGui.QPainterPath: ...
    def modifierMask(self) -> PySide6.QtCore.Qt.KeyboardModifier: ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None: ...
    def setButton(self, button: PySide6.QtCore.Qt.MouseButton) -> None: ...
    def setHitTestPath(self, path: PySide6.QtGui.QPainterPath) -> None: ...
    def setModifierMask(self, modifiers: PySide6.QtCore.Qt.KeyboardModifier) -> None: ...


class QSignalTransition(PySide6.QtStateMachine.QAbstractTransition):

    @overload
    def __init__(self, arg__1: object, arg__2: Optional[PySide6.QtStateMachine.QState] = ...) -> PySide6.QtStateMachine.QSignalTransition: ...
    @overload
    def __init__(self, sender: PySide6.QtCore.QObject, signal: bytes, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, sourceState: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None: ...
    def senderObject(self) -> PySide6.QtCore.QObject: ...
    def setSenderObject(self, sender: PySide6.QtCore.QObject) -> None: ...
    def setSignal(self, signal: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def signal(self) -> PySide6.QtCore.QByteArray: ...


class QState(PySide6.QtStateMachine.QAbstractState):

    class ChildMode(shibokensupport.enum_310.Enum):

        ExclusiveStates          : QState.ChildMode = ... # 0x0
        ParallelStates           : QState.ChildMode = ... # 0x1


    class RestorePolicy(shibokensupport.enum_310.Enum):

        DontRestoreProperties    : QState.RestorePolicy = ... # 0x0
        RestoreProperties        : QState.RestorePolicy = ... # 0x1


    @overload
    def __init__(self, childMode: PySide6.QtStateMachine.QState.ChildMode, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtStateMachine.QState] = ...) -> None: ...

    @overload
    def addTransition(self, arg__1: object, arg__2: PySide6.QtStateMachine.QAbstractState) -> PySide6.QtStateMachine.QSignalTransition: ...
    @overload
    def addTransition(self, sender: PySide6.QtCore.QObject, signal: bytes, target: PySide6.QtStateMachine.QAbstractState) -> PySide6.QtStateMachine.QSignalTransition: ...
    @overload
    def addTransition(self, target: PySide6.QtStateMachine.QAbstractState) -> PySide6.QtStateMachine.QAbstractTransition: ...
    @overload
    def addTransition(self, transition: PySide6.QtStateMachine.QAbstractTransition) -> None: ...
    def assignProperty(self, object: PySide6.QtCore.QObject, name: bytes, value: Any) -> None: ...
    def childMode(self) -> PySide6.QtStateMachine.QState.ChildMode: ...
    def errorState(self) -> PySide6.QtStateMachine.QAbstractState: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def initialState(self) -> PySide6.QtStateMachine.QAbstractState: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None: ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None: ...
    def removeTransition(self, transition: PySide6.QtStateMachine.QAbstractTransition) -> None: ...
    def setChildMode(self, mode: PySide6.QtStateMachine.QState.ChildMode) -> None: ...
    def setErrorState(self, state: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def setInitialState(self, state: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def transitions(self) -> List[PySide6.QtStateMachine.QAbstractTransition]: ...


class QStateMachine(PySide6.QtStateMachine.QState):

    class Error(shibokensupport.enum_310.Enum):

        NoError                  : QStateMachine.Error = ... # 0x0
        NoInitialStateError      : QStateMachine.Error = ... # 0x1
        NoDefaultStateInHistoryStateError: QStateMachine.Error = ... # 0x2
        NoCommonAncestorForTransitionError: QStateMachine.Error = ... # 0x3
        StateMachineChildModeSetToParallelError: QStateMachine.Error = ... # 0x4


    class EventPriority(shibokensupport.enum_310.Enum):

        NormalPriority           : QStateMachine.EventPriority = ... # 0x0
        HighPriority             : QStateMachine.EventPriority = ... # 0x1


    class SignalEvent(PySide6.QtCore.QEvent):

        def __init__(self, sender: PySide6.QtCore.QObject, signalIndex: int, arguments: Sequence[Any]) -> None: ...

        def arguments(self) -> List[Any]: ...
        def sender(self) -> PySide6.QtCore.QObject: ...
        def signalIndex(self) -> int: ...

    class WrappedEvent(PySide6.QtCore.QEvent):

        def __init__(self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> None: ...

        def event(self) -> PySide6.QtCore.QEvent: ...
        def object(self) -> PySide6.QtCore.QObject: ...


    @overload
    def __init__(self, childMode: PySide6.QtStateMachine.QState.ChildMode, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def addDefaultAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None: ...
    def addState(self, state: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def beginMicrostep(self, event: PySide6.QtCore.QEvent) -> None: ...
    def beginSelectTransitions(self, event: PySide6.QtCore.QEvent) -> None: ...
    def cancelDelayedEvent(self, id: int) -> bool: ...
    def clearError(self) -> None: ...
    def configuration(self) -> Set[PySide6.QtStateMachine.QAbstractState]: ...
    def defaultAnimations(self) -> List[PySide6.QtCore.QAbstractAnimation]: ...
    def endMicrostep(self, event: PySide6.QtCore.QEvent) -> None: ...
    def endSelectTransitions(self, event: PySide6.QtCore.QEvent) -> None: ...
    def error(self) -> PySide6.QtStateMachine.QStateMachine.Error: ...
    def errorString(self) -> str: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...
    def globalRestorePolicy(self) -> PySide6.QtStateMachine.QState.RestorePolicy: ...
    def isAnimated(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None: ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None: ...
    def postDelayedEvent(self, event: PySide6.QtCore.QEvent, delay: int) -> int: ...
    def postEvent(self, event: PySide6.QtCore.QEvent, priority: PySide6.QtStateMachine.QStateMachine.EventPriority = ...) -> None: ...
    def removeDefaultAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None: ...
    def removeState(self, state: PySide6.QtStateMachine.QAbstractState) -> None: ...
    def setAnimated(self, enabled: bool) -> None: ...
    def setGlobalRestorePolicy(self, restorePolicy: PySide6.QtStateMachine.QState.RestorePolicy) -> None: ...
    def setRunning(self, running: bool) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


# eof
