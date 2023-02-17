# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtQuick3D, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtQuick3D`

import PySide6.QtQuick3D
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtQml

import enum
from typing import Any, Optional, Tuple, Union, List, overload
from shiboken6 import Shiboken


class QIntList(object): ...


class QQuick3D(Shiboken.Object):

    def __init__(self) -> None: ...

    @staticmethod
    def idealSurfaceFormat(samples: int = ...) -> PySide6.QtGui.QSurfaceFormat: ...


class QQuick3DGeometry(PySide6.QtQuick3D.QQuick3DObject):

    geometryNodeDirty: PySide6.QtCore.Signal


    class Attribute(Shiboken.Object):

        class ComponentType(enum.Enum):

            U16Type                  : QQuick3DGeometry.Attribute.ComponentType = ... # 0x0
            U32Type                  : QQuick3DGeometry.Attribute.ComponentType = ... # 0x1
            I32Type                  : QQuick3DGeometry.Attribute.ComponentType = ... # 0x2
            F32Type                  : QQuick3DGeometry.Attribute.ComponentType = ... # 0x3


        class Semantic(enum.Enum):

            IndexSemantic            : QQuick3DGeometry.Attribute.Semantic = ... # 0x0
            PositionSemantic         : QQuick3DGeometry.Attribute.Semantic = ... # 0x1
            NormalSemantic           : QQuick3DGeometry.Attribute.Semantic = ... # 0x2
            TexCoord0Semantic        : QQuick3DGeometry.Attribute.Semantic = ... # 0x3
            TexCoordSemantic         : QQuick3DGeometry.Attribute.Semantic = ... # 0x3
            TangentSemantic          : QQuick3DGeometry.Attribute.Semantic = ... # 0x4
            BinormalSemantic         : QQuick3DGeometry.Attribute.Semantic = ... # 0x5
            JointSemantic            : QQuick3DGeometry.Attribute.Semantic = ... # 0x6
            WeightSemantic           : QQuick3DGeometry.Attribute.Semantic = ... # 0x7
            ColorSemantic            : QQuick3DGeometry.Attribute.Semantic = ... # 0x8
            TargetPositionSemantic   : QQuick3DGeometry.Attribute.Semantic = ... # 0x9
            TargetNormalSemantic     : QQuick3DGeometry.Attribute.Semantic = ... # 0xa
            TargetTangentSemantic    : QQuick3DGeometry.Attribute.Semantic = ... # 0xb
            TargetBinormalSemantic   : QQuick3DGeometry.Attribute.Semantic = ... # 0xc
            TexCoord1Semantic        : QQuick3DGeometry.Attribute.Semantic = ... # 0xd


        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, Attribute: PySide6.QtQuick3D.QQuick3DGeometry.Attribute) -> None: ...

        @staticmethod
        def __copy__() -> None: ...

    class PrimitiveType(enum.Enum):

        Points                   : QQuick3DGeometry.PrimitiveType = ... # 0x0
        LineStrip                : QQuick3DGeometry.PrimitiveType = ... # 0x1
        Lines                    : QQuick3DGeometry.PrimitiveType = ... # 0x2
        TriangleStrip            : QQuick3DGeometry.PrimitiveType = ... # 0x3
        TriangleFan              : QQuick3DGeometry.PrimitiveType = ... # 0x4
        Triangles                : QQuick3DGeometry.PrimitiveType = ... # 0x5


    def __init__(self, parent: Optional[PySide6.QtQuick3D.QQuick3DObject] = ...) -> None: ...

    @overload
    def addAttribute(self, att: PySide6.QtQuick3D.QQuick3DGeometry.Attribute) -> None: ...
    @overload
    def addAttribute(self, semantic: PySide6.QtQuick3D.QQuick3DGeometry.Attribute.Semantic, offset: int, componentType: PySide6.QtQuick3D.QQuick3DGeometry.Attribute.ComponentType) -> None: ...
    def addSubset(self, offset: int, count: int, boundsMin: PySide6.QtGui.QVector3D, boundsMax: PySide6.QtGui.QVector3D, name: str = ...) -> None: ...
    def attribute(self, index: int) -> PySide6.QtQuick3D.QQuick3DGeometry.Attribute: ...
    def attributeCount(self) -> int: ...
    def boundsMax(self) -> PySide6.QtGui.QVector3D: ...
    def boundsMin(self) -> PySide6.QtGui.QVector3D: ...
    def clear(self) -> None: ...
    def indexData(self) -> PySide6.QtCore.QByteArray: ...
    def markAllDirty(self) -> None: ...
    def primitiveType(self) -> PySide6.QtQuick3D.QQuick3DGeometry.PrimitiveType: ...
    def setBounds(self, min: PySide6.QtGui.QVector3D, max: PySide6.QtGui.QVector3D) -> None: ...
    @overload
    def setIndexData(self, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    @overload
    def setIndexData(self, offset: int, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def setPrimitiveType(self, type: PySide6.QtQuick3D.QQuick3DGeometry.PrimitiveType) -> None: ...
    def setStride(self, stride: int) -> None: ...
    @overload
    def setVertexData(self, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    @overload
    def setVertexData(self, offset: int, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def stride(self) -> int: ...
    def subsetBoundsMax(self, subset: int) -> PySide6.QtGui.QVector3D: ...
    def subsetBoundsMin(self, subset: int) -> PySide6.QtGui.QVector3D: ...
    @overload
    def subsetCount(self) -> int: ...
    @overload
    def subsetCount(self, subset: int) -> int: ...
    def subsetName(self, subset: int) -> str: ...
    def subsetOffset(self, subset: int) -> int: ...
    def vertexData(self) -> PySide6.QtCore.QByteArray: ...


class QQuick3DInstancing(PySide6.QtQuick3D.QQuick3DObject):

    depthSortingEnabledChanged: PySide6.QtCore.Signal
    hasTransparencyChanged: PySide6.QtCore.Signal
    instanceCountOverrideChanged: PySide6.QtCore.Signal
    instanceNodeDirty: PySide6.QtCore.Signal
    instanceTableChanged: PySide6.QtCore.Signal


    class InstanceTableEntry(Shiboken.Object):

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, InstanceTableEntry: PySide6.QtQuick3D.QQuick3DInstancing.InstanceTableEntry) -> None: ...

        @staticmethod
        def __copy__() -> None: ...
        def getColor(self) -> PySide6.QtGui.QColor: ...
        def getPosition(self) -> PySide6.QtGui.QVector3D: ...
        def getRotation(self) -> PySide6.QtGui.QQuaternion: ...
        def getScale(self) -> PySide6.QtGui.QVector3D: ...


    def __init__(self, parent: Optional[PySide6.QtQuick3D.QQuick3DObject] = ...) -> None: ...

    @staticmethod
    def calculateTableEntry(position: PySide6.QtGui.QVector3D, scale: PySide6.QtGui.QVector3D, eulerRotation: PySide6.QtGui.QVector3D, color: Union[PySide6.QtGui.QColor, PySide6.QtGui.QRgba64, Any, PySide6.QtCore.Qt.GlobalColor, str, int], customData: PySide6.QtGui.QVector4D = ...) -> PySide6.QtQuick3D.QQuick3DInstancing.InstanceTableEntry: ...
    @staticmethod
    def calculateTableEntryFromQuaternion(position: PySide6.QtGui.QVector3D, scale: PySide6.QtGui.QVector3D, rotation: PySide6.QtGui.QQuaternion, color: Union[PySide6.QtGui.QColor, PySide6.QtGui.QRgba64, Any, PySide6.QtCore.Qt.GlobalColor, str, int], customData: PySide6.QtGui.QVector4D = ...) -> PySide6.QtQuick3D.QQuick3DInstancing.InstanceTableEntry: ...
    def depthSortingEnabled(self) -> bool: ...
    def getInstanceBuffer(self) -> Tuple[PySide6.QtCore.QByteArray, int]: ...
    def hasTransparency(self) -> bool: ...
    def instanceBuffer(self) -> Tuple[PySide6.QtCore.QByteArray, int]: ...
    def instanceColor(self, index: int) -> PySide6.QtGui.QColor: ...
    def instanceCountOverride(self) -> int: ...
    def instanceCustomData(self, index: int) -> PySide6.QtGui.QVector4D: ...
    def instancePosition(self, index: int) -> PySide6.QtGui.QVector3D: ...
    def instanceRotation(self, index: int) -> PySide6.QtGui.QQuaternion: ...
    def instanceScale(self, index: int) -> PySide6.QtGui.QVector3D: ...
    def markDirty(self) -> None: ...
    def setDepthSortingEnabled(self, enabled: bool) -> None: ...
    def setHasTransparency(self, hasTransparency: bool) -> None: ...
    def setInstanceCountOverride(self, instanceCountOverride: int) -> None: ...


class QQuick3DObject(PySide6.QtCore.QObject, PySide6.QtQml.QQmlParserStatus):

    childrenChanged: PySide6.QtCore.Signal
    parentChanged: PySide6.QtCore.Signal
    stateChanged: PySide6.QtCore.Signal


    class ItemChange(enum.Enum):

        ItemChildAddedChange     : QQuick3DObject.ItemChange = ... # 0x0
        ItemChildRemovedChange   : QQuick3DObject.ItemChange = ... # 0x1
        ItemSceneChange          : QQuick3DObject.ItemChange = ... # 0x2
        ItemVisibleHasChanged    : QQuick3DObject.ItemChange = ... # 0x3
        ItemParentHasChanged     : QQuick3DObject.ItemChange = ... # 0x4
        ItemOpacityHasChanged    : QQuick3DObject.ItemChange = ... # 0x5
        ItemActiveFocusHasChanged: QQuick3DObject.ItemChange = ... # 0x6
        ItemRotationHasChanged   : QQuick3DObject.ItemChange = ... # 0x7
        ItemAntialiasingHasChanged: QQuick3DObject.ItemChange = ... # 0x8
        ItemDevicePixelRatioHasChanged: QQuick3DObject.ItemChange = ... # 0x9
        ItemEnabledHasChanged    : QQuick3DObject.ItemChange = ... # 0xa


    def childItems(self) -> List[PySide6.QtQuick3D.QQuick3DObject]: ...
    def classBegin(self) -> None: ...
    def componentComplete(self) -> None: ...
    def isComponentComplete(self) -> bool: ...
    def markAllDirty(self) -> None: ...
    def parentItem(self) -> PySide6.QtQuick3D.QQuick3DObject: ...
    def preSync(self) -> None: ...
    def setParentItem(self, parentItem: PySide6.QtQuick3D.QQuick3DObject) -> None: ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...
    def update(self) -> None: ...


class QQuick3DTextureData(PySide6.QtQuick3D.QQuick3DObject):

    textureDataNodeDirty: PySide6.QtCore.Signal


    class Format(enum.Enum):

        None_                    : QQuick3DTextureData.Format = ... # 0x0
        RGBA8                    : QQuick3DTextureData.Format = ... # 0x1
        RGBA16F                  : QQuick3DTextureData.Format = ... # 0x2
        RGBA32F                  : QQuick3DTextureData.Format = ... # 0x3
        RGBE8                    : QQuick3DTextureData.Format = ... # 0x4
        R8                       : QQuick3DTextureData.Format = ... # 0x5
        R16                      : QQuick3DTextureData.Format = ... # 0x6
        R16F                     : QQuick3DTextureData.Format = ... # 0x7
        R32F                     : QQuick3DTextureData.Format = ... # 0x8
        BC1                      : QQuick3DTextureData.Format = ... # 0x9
        BC2                      : QQuick3DTextureData.Format = ... # 0xa
        BC3                      : QQuick3DTextureData.Format = ... # 0xb
        BC4                      : QQuick3DTextureData.Format = ... # 0xc
        BC5                      : QQuick3DTextureData.Format = ... # 0xd
        BC6H                     : QQuick3DTextureData.Format = ... # 0xe
        BC7                      : QQuick3DTextureData.Format = ... # 0xf
        DXT1_RGBA                : QQuick3DTextureData.Format = ... # 0x10
        DXT1_RGB                 : QQuick3DTextureData.Format = ... # 0x11
        DXT3_RGBA                : QQuick3DTextureData.Format = ... # 0x12
        DXT5_RGBA                : QQuick3DTextureData.Format = ... # 0x13
        ETC2_RGB8                : QQuick3DTextureData.Format = ... # 0x14
        ETC2_RGB8A1              : QQuick3DTextureData.Format = ... # 0x15
        ETC2_RGBA8               : QQuick3DTextureData.Format = ... # 0x16
        ASTC_4x4                 : QQuick3DTextureData.Format = ... # 0x17
        ASTC_5x4                 : QQuick3DTextureData.Format = ... # 0x18
        ASTC_5x5                 : QQuick3DTextureData.Format = ... # 0x19
        ASTC_6x5                 : QQuick3DTextureData.Format = ... # 0x1a
        ASTC_6x6                 : QQuick3DTextureData.Format = ... # 0x1b
        ASTC_8x5                 : QQuick3DTextureData.Format = ... # 0x1c
        ASTC_8x6                 : QQuick3DTextureData.Format = ... # 0x1d
        ASTC_8x8                 : QQuick3DTextureData.Format = ... # 0x1e
        ASTC_10x5                : QQuick3DTextureData.Format = ... # 0x1f
        ASTC_10x6                : QQuick3DTextureData.Format = ... # 0x20
        ASTC_10x8                : QQuick3DTextureData.Format = ... # 0x21
        ASTC_10x10               : QQuick3DTextureData.Format = ... # 0x22
        ASTC_12x10               : QQuick3DTextureData.Format = ... # 0x23
        ASTC_12x12               : QQuick3DTextureData.Format = ... # 0x24


    def __init__(self, parent: Optional[PySide6.QtQuick3D.QQuick3DObject] = ...) -> None: ...

    def format(self) -> PySide6.QtQuick3D.QQuick3DTextureData.Format: ...
    def hasTransparency(self) -> bool: ...
    def markAllDirty(self) -> None: ...
    def setFormat(self, format: PySide6.QtQuick3D.QQuick3DTextureData.Format) -> None: ...
    def setHasTransparency(self, hasTransparency: bool) -> None: ...
    def setSize(self, size: PySide6.QtCore.QSize) -> None: ...
    def setTextureData(self, data: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    def size(self) -> PySide6.QtCore.QSize: ...
    def textureData(self) -> PySide6.QtCore.QByteArray: ...


# eof
