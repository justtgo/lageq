# lageq.ro

Site static pentru **la geq** – benzile desenate Elo & Elo, generat din vechiul WordPress (tema ePortfolio).
Fără build, fără dependențe: sunt doar fișiere HTML, CSS, JS și imagini.

## Publicare pe Netlify
1. Add new site → Import an existing project → GitHub → alege acest repo.
2. Build command: gol. Publish directory: `.`
3. Deploy. Setările (redirecturi, headere) sunt în `netlify.toml` și `_headers`.

Fiecare `git push` pe `main` republică site-ul automat.

## Domeniu
Canonical, sitemap și Open Graph folosesc `https://lageq.ro`.
Dacă publici întâi pe alt domeniu (ex. `nume.netlify.app`):

```
python3 set-domain.py https://nume.netlify.app
```

Rulează scriptul din nou când treci pe domeniul final, apoi fă commit.

## Structura
| Cale | Ce conține |
|---|---|
| `index.html`, `page/` | pagina principală și paginarea |
| `<slug>/index.html` | articolele (ex. `rewind/`, `my-story/`) |
| `category/` | paginile de categorii |
| `wp-content/uploads/` | imaginile originale; `opt/` conține versiunile WebP responsive |
| `wp-content/themes/eportfolio/` | CSS și JS din tema originală |
| `custom.css` | ajustările făcute peste temă (mobil, navigare, carduri) |
| `sitemap.xml`, `robots.txt`, `feed.xml` | SEO și RSS |
| `404.html` | pagina de eroare |

## SEO
Titluri și descrieri unice, canonical, Open Graph și Twitter Cards, JSON-LD (WebSite, BlogPosting, BreadcrumbList),
un singur `<h1>` pe pagină, alt text pe imagini, redirecturi de la URL-urile vechi WordPress.
După publicare, adaugă site-ul în Google Search Console și trimite `sitemap.xml`.

## De completat
- `wp-content/uploads/2025/01/design-task.pdf` lipsește (butonul „Explore The Output" din articolul „Looks awesome!").
- Fonturile (Google Fonts) și avatarul (Gravatar) se încarcă de pe internet.
