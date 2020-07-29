from modules.ms.microsoft_graph import MicrosoftGraph
from modules.ms.one_note.notebook import Notebook


class OneNote:
  def __init__(self):
    self._ms = MicrosoftGraph()
    self._root = "https://graph.microsoft.com/v1.0/me/onenote/"
    self._notebooks = []

  def _getAllNotebooks(self):
    all_notebooks_query = self._root + "notebooks"
    notebooks = self._ms.request(all_notebooks_query)['value']
    return notebooks

  def _getNotebook(self, notebook_name: str):
    notebooks = self._getAllNotebooks()
    found_notebook = next((notebook for notebook in notebooks if
                           notebook["displayName"] == notebook_name), None)
    if found_notebook is not None:
      return Notebook(self._ms, found_notebook)
    else:
      return None

  # Pack notebooks into list of Notebook class
  def _getAllNotebooks(self):
    all_notebooks_query = self._root + "notebooks"
    notebooks = self._ms.request(all_notebooks_query)['value']
    return notebooks

  # TODO extend for ability get notebook, section and work with them
  def get_page(self, notebook, section, pageName):
    notebook = self._getNotebook(notebook)
    section = notebook.getSection(section)
    page = section.getPage(pageName)
    return page
