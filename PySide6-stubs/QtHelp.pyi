#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
"""
This file contains the exact signatures for all functions in module
PySide6.QtHelp, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtHelp`

import PySide6.QtHelp
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from enum import Enum
from typing import Any, Optional, Tuple, Union, Sequence, Dict, List, overload
from shiboken6 import Shiboken


class QCompressedHelpInfo(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtHelp.QCompressedHelpInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def component(self) -> str: ...
    @staticmethod
    def fromCompressedHelpFile(documentationFileName:str) -> PySide6.QtHelp.QCompressedHelpInfo: ...
    def isNull(self) -> bool: ...
    def namespaceName(self) -> str: ...
    def swap(self, other:PySide6.QtHelp.QCompressedHelpInfo) -> None: ...
    def version(self) -> PySide6.QtCore.QVersionNumber: ...


class QHelpContentItem(Shiboken.Object):

    def __init__(self, QHelpContentItem:PySide6.QtHelp.QHelpContentItem) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def child(self, row:int) -> PySide6.QtHelp.QHelpContentItem: ...
    def childCount(self) -> int: ...
    def childPosition(self, child:PySide6.QtHelp.QHelpContentItem) -> int: ...
    def parent(self) -> PySide6.QtHelp.QHelpContentItem: ...
    def row(self) -> int: ...
    def title(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...


class QHelpContentModel(PySide6.QtCore.QAbstractItemModel):
    def columnCount(self, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> int: ...
    def contentItemAt(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtHelp.QHelpContentItem: ...
    def createContents(self, customFilterName:str) -> None: ...
    def data(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role:int) -> Any: ...
    def index(self, row:int, column:int, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> PySide6.QtCore.QModelIndex: ...
    def isCreatingContents(self) -> bool: ...
    @overload
    def parent(self) -> PySide6.QtCore.QObject: ...
    @overload
    def parent(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.QModelIndex: ...
    def rowCount(self, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> int: ...


class QHelpContentWidget(PySide6.QtWidgets.QTreeView):
    def indexOf(self, link:Union[PySide6.QtCore.QUrl, str]) -> PySide6.QtCore.QModelIndex: ...


class QHelpEngine(PySide6.QtHelp.QHelpEngineCore):

    def __init__(self, collectionFile:str, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def contentModel(self) -> PySide6.QtHelp.QHelpContentModel: ...
    def contentWidget(self) -> PySide6.QtHelp.QHelpContentWidget: ...
    def indexModel(self) -> PySide6.QtHelp.QHelpIndexModel: ...
    def indexWidget(self) -> PySide6.QtHelp.QHelpIndexWidget: ...
    def searchEngine(self) -> PySide6.QtHelp.QHelpSearchEngine: ...


class QHelpEngineCore(PySide6.QtCore.QObject):

    def __init__(self, collectionFile:str, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def addCustomFilter(self, filterName:str, attributes:Sequence[str]) -> bool: ...
    def autoSaveFilter(self) -> bool: ...
    def collectionFile(self) -> str: ...
    def copyCollectionFile(self, fileName:str) -> bool: ...
    def currentFilter(self) -> str: ...
    def customFilters(self) -> List[str]: ...
    def customValue(self, key:str, defaultValue:Any=...) -> Any: ...
    def documentationFileName(self, namespaceName:str) -> str: ...
    @overload
    def documentsForIdentifier(self, id:str) -> List[PySide6.QtHelp.QHelpLink]: ...
    @overload
    def documentsForIdentifier(self, id:str, filterName:str) -> List[PySide6.QtHelp.QHelpLink]: ...
    @overload
    def documentsForKeyword(self, keyword:str) -> List[PySide6.QtHelp.QHelpLink]: ...
    @overload
    def documentsForKeyword(self, keyword:str, filterName:str) -> List[PySide6.QtHelp.QHelpLink]: ...
    def error(self) -> str: ...
    def fileData(self, url:Union[PySide6.QtCore.QUrl, str]) -> PySide6.QtCore.QByteArray: ...
    @overload
    def files(self, namespaceName:str, filterAttributes:Sequence[str], extensionFilter:str=...) -> List[PySide6.QtCore.QUrl]: ...
    @overload
    def files(self, namespaceName:str, filterName:str, extensionFilter:str=...) -> List[PySide6.QtCore.QUrl]: ...
    def filterAttributeSets(self, namespaceName:str) -> List[List[str]]: ...
    @overload
    def filterAttributes(self) -> List[str]: ...
    @overload
    def filterAttributes(self, filterName:str) -> List[str]: ...
    def filterEngine(self) -> PySide6.QtHelp.QHelpFilterEngine: ...
    def findFile(self, url:Union[PySide6.QtCore.QUrl, str]) -> PySide6.QtCore.QUrl: ...
    def isReadOnly(self) -> bool: ...
    @staticmethod
    def metaData(documentationFileName:str, name:str) -> Any: ...
    @staticmethod
    def namespaceName(documentationFileName:str) -> str: ...
    def registerDocumentation(self, documentationFileName:str) -> bool: ...
    def registeredDocumentations(self) -> List[str]: ...
    def removeCustomFilter(self, filterName:str) -> bool: ...
    def removeCustomValue(self, key:str) -> bool: ...
    def setAutoSaveFilter(self, save:bool) -> None: ...
    def setCollectionFile(self, fileName:str) -> None: ...
    def setCurrentFilter(self, filterName:str) -> None: ...
    def setCustomValue(self, key:str, value:Any) -> bool: ...
    def setReadOnly(self, enable:bool) -> None: ...
    def setUsesFilterEngine(self, uses:bool) -> None: ...
    def setupData(self) -> bool: ...
    def unregisterDocumentation(self, namespaceName:str) -> bool: ...
    def usesFilterEngine(self) -> bool: ...


class QHelpFilterData(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtHelp.QHelpFilterData) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def components(self) -> List[str]: ...
    def setComponents(self, components:Sequence[str]) -> None: ...
    def setVersions(self, versions:Sequence[PySide6.QtCore.QVersionNumber]) -> None: ...
    def swap(self, other:PySide6.QtHelp.QHelpFilterData) -> None: ...
    def versions(self) -> List[PySide6.QtCore.QVersionNumber]: ...


class QHelpFilterEngine(PySide6.QtCore.QObject):

    def __init__(self, helpEngine:PySide6.QtHelp.QHelpEngineCore) -> None: ...

    def activeFilter(self) -> str: ...
    def availableComponents(self) -> List[str]: ...
    def availableVersions(self) -> List[PySide6.QtCore.QVersionNumber]: ...
    def filterData(self, filterName:str) -> PySide6.QtHelp.QHelpFilterData: ...
    def filters(self) -> List[str]: ...
    @overload
    def indices(self) -> List[str]: ...
    @overload
    def indices(self, filterName:str) -> List[str]: ...
    def namespaceToComponent(self) -> Dict[str, str]: ...
    def namespaceToVersion(self) -> Dict[str, PySide6.QtCore.QVersionNumber]: ...
    def namespacesForFilter(self, filterName:str) -> List[str]: ...
    def removeFilter(self, filterName:str) -> bool: ...
    def setActiveFilter(self, filterName:str) -> bool: ...
    def setFilterData(self, filterName:str, filterData:PySide6.QtHelp.QHelpFilterData) -> bool: ...


class QHelpFilterSettingsWidget(PySide6.QtWidgets.QWidget):

    def __init__(self, parent:Optional[PySide6.QtWidgets.QWidget]=...) -> None: ...

    def applySettings(self, filterEngine:PySide6.QtHelp.QHelpFilterEngine) -> bool: ...
    def readSettings(self, filterEngine:PySide6.QtHelp.QHelpFilterEngine) -> None: ...
    def setAvailableComponents(self, components:Sequence[str]) -> None: ...
    def setAvailableVersions(self, versions:Sequence[PySide6.QtCore.QVersionNumber]) -> None: ...


class QHelpIndexModel(PySide6.QtCore.QStringListModel):
    def createIndex(self, customFilterName:str) -> None: ...
    def filter(self, filter:str, wildcard:str=...) -> PySide6.QtCore.QModelIndex: ...
    def helpEngine(self) -> PySide6.QtHelp.QHelpEngineCore: ...
    def isCreatingIndex(self) -> bool: ...


class QHelpIndexWidget(PySide6.QtWidgets.QListView):
    def activateCurrentItem(self) -> None: ...
    def filterIndices(self, filter:str, wildcard:str=...) -> None: ...


class QHelpLink(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QHelpLink:PySide6.QtHelp.QHelpLink) -> None: ...

    @staticmethod
    def __copy__() -> None: ...


class QHelpSearchEngine(PySide6.QtCore.QObject):

    def __init__(self, helpEngine:PySide6.QtHelp.QHelpEngineCore, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def cancelIndexing(self) -> None: ...
    def cancelSearching(self) -> None: ...
    def hitCount(self) -> int: ...
    def hits(self, start:int, end:int) -> List[Tuple[str, str]]: ...
    def hitsCount(self) -> int: ...
    def query(self) -> List[PySide6.QtHelp.QHelpSearchQuery]: ...
    def queryWidget(self) -> PySide6.QtHelp.QHelpSearchQueryWidget: ...
    def reindexDocumentation(self) -> None: ...
    def resultWidget(self) -> PySide6.QtHelp.QHelpSearchResultWidget: ...
    def scheduleIndexDocumentation(self) -> None: ...
    @overload
    def search(self, queryList:Sequence[PySide6.QtHelp.QHelpSearchQuery]) -> None: ...
    @overload
    def search(self, searchInput:str) -> None: ...
    def searchInput(self) -> str: ...
    def searchResultCount(self) -> int: ...
    def searchResults(self, start:int, end:int) -> List[PySide6.QtHelp.QHelpSearchResult]: ...


class QHelpSearchQuery(Shiboken.Object):

    DEFAULT                  : QHelpSearchQuery.FieldName = ... # 0x0
    FUZZY                    : QHelpSearchQuery.FieldName = ... # 0x1
    WITHOUT                  : QHelpSearchQuery.FieldName = ... # 0x2
    PHRASE                   : QHelpSearchQuery.FieldName = ... # 0x3
    ALL                      : QHelpSearchQuery.FieldName = ... # 0x4
    ATLEAST                  : QHelpSearchQuery.FieldName = ... # 0x5

    class FieldName(Enum):

        DEFAULT                  : QHelpSearchQuery.FieldName = ... # 0x0
        FUZZY                    : QHelpSearchQuery.FieldName = ... # 0x1
        WITHOUT                  : QHelpSearchQuery.FieldName = ... # 0x2
        PHRASE                   : QHelpSearchQuery.FieldName = ... # 0x3
        ALL                      : QHelpSearchQuery.FieldName = ... # 0x4
        ATLEAST                  : QHelpSearchQuery.FieldName = ... # 0x5


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QHelpSearchQuery:PySide6.QtHelp.QHelpSearchQuery) -> None: ...
    @overload
    def __init__(self, field:PySide6.QtHelp.QHelpSearchQuery.FieldName, wordList_:Sequence[str]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...


class QHelpSearchQueryWidget(PySide6.QtWidgets.QWidget):

    def __init__(self, parent:Optional[PySide6.QtWidgets.QWidget]=...) -> None: ...

    def changeEvent(self, event:PySide6.QtCore.QEvent) -> None: ...
    def collapseExtendedSearch(self) -> None: ...
    def expandExtendedSearch(self) -> None: ...
    def focusInEvent(self, focusEvent:PySide6.QtGui.QFocusEvent) -> None: ...
    def isCompactMode(self) -> bool: ...
    def query(self) -> List[PySide6.QtHelp.QHelpSearchQuery]: ...
    def searchInput(self) -> str: ...
    def setCompactMode(self, on:bool) -> None: ...
    def setQuery(self, queryList:Sequence[PySide6.QtHelp.QHelpSearchQuery]) -> None: ...
    def setSearchInput(self, searchInput:str) -> None: ...


class QHelpSearchResult(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtHelp.QHelpSearchResult) -> None: ...
    @overload
    def __init__(self, url:Union[PySide6.QtCore.QUrl, str], title:str, snippet:str) -> None: ...

    def snippet(self) -> str: ...
    def title(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...


class QHelpSearchResultWidget(PySide6.QtWidgets.QWidget):
    def changeEvent(self, event:PySide6.QtCore.QEvent) -> None: ...
    def linkAt(self, point:PySide6.QtCore.QPoint) -> PySide6.QtCore.QUrl: ...


class QIntList(object): ...


# eof
