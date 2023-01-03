# Architecture

# Main functionalities

These two sequence diagrams were created in the first sprint to help build a common understanding of how the user stories selected for the sprint are to be built.

```mermaid
sequenceDiagram
actor user
participant UI
participant ReferenceService
participant ArticleEntity
participant ReferenceRepository

user ->> UI: selects 'new article'
UI ->> ReferenceService: create_new(article)
ReferenceService ->> ArticleEntity: new article_object()
activate ReferenceService
ReferenceService ->> UI: entry types
ReferenceService ->> ReferenceService: Loop through entry types.
deactivate ReferenceService
ReferenceService ->> ReferenceRepository: try to store_object(article_object)
ReferenceService ->> UI: notify user of success / error
UI ->> user: gets notification
```

```mermaid
sequenceDiagram
actor user
participant UI
participant ReferenceService
participant ArticleEntity
participant ReferenceRepository

user ->> UI: selects 'view references'
UI ->> ReferenceService: get_all_references()
ReferenceService ->> ReferenceRepository: get_all_references()
ReferenceRepository -->> ReferenceService: return references [list of dictionaries]
ReferenceService ->> UI: return references as [list of dictionaries]
UI ->> user: output references
```
