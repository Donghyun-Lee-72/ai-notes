function normalizePath(url) {
  const path = new URL(url, window.location.href).pathname;
  return path.endsWith("/") ? path : `${path}/`;
}

function buildTabMenus() {
  const primaryNavigation = document.querySelector(
    '.md-sidebar--primary nav[data-md-level="0"]'
  );

  if (!primaryNavigation) return;

  document.querySelectorAll(".md-tabs__item").forEach((tab) => {
    if (tab.querySelector(".ai-tab-menu")) return;

    const tabLink = tab.querySelector(":scope > .md-tabs__link");
    if (!tabLink) return;

    const tabPath = normalizePath(tabLink.href);
    const matchingLink = Array.from(
      primaryNavigation.querySelectorAll("a.md-nav__link")
    ).find((link) => normalizePath(link.href) === tabPath);

    const section = matchingLink?.closest(".md-nav__item--nested");
    const nestedNavigation = section?.querySelector(":scope > nav");
    if (!nestedNavigation) return;

    const links = Array.from(
      nestedNavigation.querySelectorAll("a.md-nav__link")
    );

    if (!links.length) return;

    const menu = document.createElement("ul");
    menu.className = "ai-tab-menu";
    if (links.length > 7) menu.classList.add("ai-tab-menu--wide");
    menu.setAttribute("aria-label", tabLink.textContent.trim());

    links.forEach((link) => {
      const item = document.createElement("li");
      const menuLink = document.createElement("a");
      menuLink.href = link.href;
      menuLink.textContent = link.textContent.trim();
      item.appendChild(menuLink);
      menu.appendChild(item);
    });

    tab.appendChild(menu);
  });
}

document.addEventListener("DOMContentLoaded", buildTabMenus);
