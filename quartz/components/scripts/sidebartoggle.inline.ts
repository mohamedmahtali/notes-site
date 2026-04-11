document.addEventListener("nav", () => {
  const collapsed = localStorage.getItem("sidebar-collapsed") === "true"
  if (collapsed) {
    document.body.classList.add("sidebar-collapsed")
  }

  const toggle = () => {
    const isCollapsed = document.body.classList.toggle("sidebar-collapsed")
    localStorage.setItem("sidebar-collapsed", String(isCollapsed))
  }

  for (const btn of document.getElementsByClassName("sidebar-toggle-btn")) {
    btn.addEventListener("click", toggle)
    window.addCleanup(() => btn.removeEventListener("click", toggle))
  }
})
