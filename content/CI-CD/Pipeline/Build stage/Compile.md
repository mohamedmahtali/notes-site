---
title: Compile
tags:
  - intermediate
---
# Compile

---

## Définition

La compilation transforme le code source en code machine ou bytecode exécutable. Dans un [[Pipeline]] CI/CD, cette étape valide que le code est syntaxiquement correct et produit un binaire avant les tests.

---

## Exemples par langage

```yaml
# Go
- name: Build Go binary
  run: |
    CGO_ENABLED=0 GOOS=linux go build -o ./bin/app ./cmd/app

# Java (Maven)
- name: Build with Maven
  run: mvn clean package -DskipTests

# TypeScript
- name: Build TypeScript
  run: |
    npm ci
    npm run build

# Rust
- name: Build Release
  run: cargo build --release
```

---

## Optimisations

```yaml
# Cache des dépendances entre builds
- name: Cache Go modules
  uses: actions/cache@v3
  with:
    path: ~/go/pkg/mod
    key: ${{ runner.os }}-go-${{ hashFiles('**/go.sum') }}
```

---

> [!tip]
> Toujours compiler avec les flags de production (`-ldflags="-w -s"` pour Go, `--release` pour Rust) dès le CI pour détecter les erreurs de build optimisé.
