const list = document.getElementById("fruit-list");

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

fetch("/api/fruits")
  .then((r) => {
    if (!r.ok) throw new Error(r.statusText);
    return r.json();
  })
  .then((fruits) => {
    list.replaceChildren();
    for (const f of fruits) {
      const card = el("li", "card");
      card.append(
        el("div", "emoji", f.emoji),
        el("h2", null, f.name),
        el("p", "local", `Malay: ${f.local_name}`),
        el("p", "tagline", f.tagline),
        el("p", null, f.description),
        el("p", "season", `Season: ${f.season}`)
      );
      list.append(card);
    }
  })
  .catch(() => {
    list.replaceChildren(el("li", "loading", "Could not load fruits."));
  });
