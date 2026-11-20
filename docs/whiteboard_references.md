# Whiteboard Diagram References

All whiteboard diagrams for the Modern Data Engineering Lakehouse Ecosystem are hosted at the following canonical URLs:

## Asset URL Patterns

| Format | URL Pattern |
|--------|-------------|
| **Primary (WebP CDN)** | `https://moderndataengineer.uk/diagrams/<slug>.webp` |
| **Fallback (GitHub Raw)** | `https://raw.githubusercontent.com/santoshjammi29/moderndataengineer/main/assets/whiteboards/<slug>.webp` |
| **Interactive Viewer** | `https://moderndataengineer.uk/whiteboards?id=<slug>` |

## Example Usage

```markdown
![Delta Lake Architecture](https://moderndataengineer.uk/diagrams/delta-lake-architecture.webp)
```

Fallback:
```markdown
![Delta Lake Architecture](https://raw.githubusercontent.com/santoshjammi29/moderndataengineer/main/assets/whiteboards/delta-lake-architecture.webp)
```

Interactive:
```
https://moderndataengineer.uk/whiteboards?id=delta-lake-architecture
```

## Slug Convention

- Slugs are lowercase, hyphen-separated, descriptive identifiers.
- Example slugs: `spark-shuffle-partitions`, `delta-lake-acid`, `kafka-partitioning-strategy`, `medallion-architecture-overview`

## Source

Whiteboard blueprints are maintained in the [moderndataengineer](https://github.com/santoshjammi29/moderndataengineer) repository under `assets/whiteboards/`.
