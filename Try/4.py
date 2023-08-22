import arxiv

# search = arxiv.Search(
#     query = "ai",
#     max_results = 10,
#     sort_by = arxiv.SortCriterion.SubmittedDate
# )

# for result in search.results():
#     print(result.title)


paper = next(arxiv.Search(id_list=["1605.08386v1"]).results())
# Download the PDF to the PWD with a default filename.
paper.download_pdf()
# Download the PDF to the PWD with a custom filename.
paper.download_pdf(filename="downloaded-paper.pdf")
# Download the PDF to a specified directory with a custom filename.
paper.download_pdf(dirpath=".", filename="downloaded-paper.pdf")