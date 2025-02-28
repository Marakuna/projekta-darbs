const tabs = document.querySelectorAll('[data-tab-target]')
const content = document.querySelectorAll('[data-tab-content]')

tabs.forEach((tab => {
  const target = document.querySelector(tab.dataset.tabTarget)
  tabContents.forEach((content => {
    content.classList.remove = 'active'
  })
  tabs.forEach(tab => {
    tab.classList.remove('active')
  })
  tab.classList.add('active')
  target.classList.add('active')
  })
})