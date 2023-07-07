# ТК#1. Выполнить неавторизованный GET-запрос (позитив)
from playwright.sync_api import sync_playwright
def test_API_1_TK_1(playwright: sync_playwright):
    query_params = {}
    query_headers = {'Authorization': ''}
    context = playwright.request.new_context(base_url='https://spb-classif.gate.petersburg.ru')
    response = context.get(url='/api/v2/datasets/172/versions/latest/data/202/', params=query_params, headers=query_headers)
    print(response)
    assert response.status == 401
    assert response.status_text == 'Unauthorized'

#ТК#2. Выполнить авторизованный GET-запрос (позитив)
from playwright.sync_api import sync_playwright
def test_API_1_TK_2(playwright: sync_playwright):
    query_params = {}
    query_headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3ODM0NDU5MjAsImlhdCI6MTY4ODc1MTUyMCwianRpIjoiMWQzNGFkODQtNDhiYS00M2JhLWJkMTgtODVlZDI0YTA2MWQwIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImQ1NDExNjBhLTk5YWItNGY2My04ZDVhLWVkZDMyNGUxYzlhOCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImJmNzEyYzM3LThiMmEtNDYzOC1iNDQ1LWIxNjE0ZmFjNjg4NSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiZjcxMmMzNy04YjJhLTQ2MzgtYjQ0NS1iMTYxNGZhYzY4ODUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQkNC90YLQvtC9INCX0Y_QsdC60LjQvSIsInByZWZlcnJlZF91c2VybmFtZSI6ImU2ODU3YWU2Y2NmZjQwMDhjYjVjNjQ4ODlmZmE0Y2Y0IiwiZ2l2ZW5fbmFtZSI6ItCQ0L3RgtC-0L0iLCJmYW1pbHlfbmFtZSI6ItCX0Y_QsdC60LjQvSJ9.zB3Xc5VYwhgYsZGMG2SSWru0fXkTezNCPawg8KXMVhs_2SA3aS_ClyGQXh117IWyrwgleCZeUU09JuJLhm1q5UqNgGHwo9HdIoeBmEyUa2oz7QRGRE2tACmP_IGCT5eiXP6jS88PXSwP3_X512CshEYpRTBrX8ST3F1fjnpz-81yp6LAJ7YCE4aoi72rjN-emZ2MzrPhZyDLe6EQ3_fAn7SMMwH0TFYZn8PKYXGOaR9nnN9Y0wWIO0nI8zMQ_DuJju8HBN55xTwwrQAPpvwoNZ47PaIVo_nFTqjwfyvwBLVAapbOv19uR8n3WzhZZDyEnMcb0oYMu59rYLLufu-pAg'}
    context = playwright.request.new_context(base_url='https://spb-classif.gate.petersburg.ru')
    response = context.get(url='/api/v2/datasets/172/versions/latest/data/202/', params=query_params, headers=query_headers)
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'

#ТК#4. Запросить некорректный Content-Type заголовка ответа (негатив)
from playwright.sync_api import sync_playwright
def test_API_1_TK_4(playwright: sync_playwright):
    query_params = {}
    query_headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3ODM0NDU5MjAsImlhdCI6MTY4ODc1MTUyMCwianRpIjoiMWQzNGFkODQtNDhiYS00M2JhLWJkMTgtODVlZDI0YTA2MWQwIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImQ1NDExNjBhLTk5YWItNGY2My04ZDVhLWVkZDMyNGUxYzlhOCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImJmNzEyYzM3LThiMmEtNDYzOC1iNDQ1LWIxNjE0ZmFjNjg4NSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiZjcxMmMzNy04YjJhLTQ2MzgtYjQ0NS1iMTYxNGZhYzY4ODUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQkNC90YLQvtC9INCX0Y_QsdC60LjQvSIsInByZWZlcnJlZF91c2VybmFtZSI6ImU2ODU3YWU2Y2NmZjQwMDhjYjVjNjQ4ODlmZmE0Y2Y0IiwiZ2l2ZW5fbmFtZSI6ItCQ0L3RgtC-0L0iLCJmYW1pbHlfbmFtZSI6ItCX0Y_QsdC60LjQvSJ9.zB3Xc5VYwhgYsZGMG2SSWru0fXkTezNCPawg8KXMVhs_2SA3aS_ClyGQXh117IWyrwgleCZeUU09JuJLhm1q5UqNgGHwo9HdIoeBmEyUa2oz7QRGRE2tACmP_IGCT5eiXP6jS88PXSwP3_X512CshEYpRTBrX8ST3F1fjnpz-81yp6LAJ7YCE4aoi72rjN-emZ2MzrPhZyDLe6EQ3_fAn7SMMwH0TFYZn8PKYXGOaR9nnN9Y0wWIO0nI8zMQ_DuJju8HBN55xTwwrQAPpvwoNZ47PaIVo_nFTqjwfyvwBLVAapbOv19uR8n3WzhZZDyEnMcb0oYMu59rYLLufu-pAg'}
    context = playwright.request.new_context(base_url='https://spb-classif.gate.petersburg.ru')
    response = context.get(url='/api/v2/datasets/172/versions/latest/data/202/', params=query_params, headers=query_headers)
    print(response)
    try:
        response.headers["content-type"] != "text/plain"
    except AssertionError:
        print('Invalid content-type: expected', response.headers["content-type"])

#TK#5. Вызвать страницу с невалидным номером (негатив)
from playwright.sync_api import sync_playwright
def test_API_2_TK_5(playwright: sync_playwright):
    query_params = {'page':'12'}
    query_headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3ODM0NDU5MjAsImlhdCI6MTY4ODc1MTUyMCwianRpIjoiMWQzNGFkODQtNDhiYS00M2JhLWJkMTgtODVlZDI0YTA2MWQwIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImQ1NDExNjBhLTk5YWItNGY2My04ZDVhLWVkZDMyNGUxYzlhOCIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImJmNzEyYzM3LThiMmEtNDYzOC1iNDQ1LWIxNjE0ZmFjNjg4NSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiZjcxMmMzNy04YjJhLTQ2MzgtYjQ0NS1iMTYxNGZhYzY4ODUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQkNC90YLQvtC9INCX0Y_QsdC60LjQvSIsInByZWZlcnJlZF91c2VybmFtZSI6ImU2ODU3YWU2Y2NmZjQwMDhjYjVjNjQ4ODlmZmE0Y2Y0IiwiZ2l2ZW5fbmFtZSI6ItCQ0L3RgtC-0L0iLCJmYW1pbHlfbmFtZSI6ItCX0Y_QsdC60LjQvSJ9.zB3Xc5VYwhgYsZGMG2SSWru0fXkTezNCPawg8KXMVhs_2SA3aS_ClyGQXh117IWyrwgleCZeUU09JuJLhm1q5UqNgGHwo9HdIoeBmEyUa2oz7QRGRE2tACmP_IGCT5eiXP6jS88PXSwP3_X512CshEYpRTBrX8ST3F1fjnpz-81yp6LAJ7YCE4aoi72rjN-emZ2MzrPhZyDLe6EQ3_fAn7SMMwH0TFYZn8PKYXGOaR9nnN9Y0wWIO0nI8zMQ_DuJju8HBN55xTwwrQAPpvwoNZ47PaIVo_nFTqjwfyvwBLVAapbOv19uR8n3WzhZZDyEnMcb0oYMu59rYLLufu-pAg'}
    context = playwright.request.new_context(base_url='https://spb-classif.gate.petersburg.ru')
    response = context.get(url='/api/v2/datasets/128/versions/latest/data/149/', params=query_params, headers=query_headers)
    print(response)

# TK#9. Передать координаты точки и лимит, сколько ближайших объектов нужно найти (позитив)
from playwright.sync_api import sync_playwright
def test_API_3_TK_9(playwright: sync_playwright):
    query_params = {'x':'30.36652', 'y':'60.00884', 'limit':'1'}
    query_headers = {'Content-Type':'application/x-www-form-urlencoded', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2a2lkMDAwMDAwMDAwIiwiZXhwIjoxNjk0NDU1Mjg5fQ.3KGoatXYEPgjy7CFMObA3au7aZMdJzoTlHPm6TmPLtI'}
    context = playwright.request.new_context(base_url='https://geointelect.gate.petersburg.ru')
    response = context.post(url='/nearest_recycling/get', params=query_params, headers=query_headers)
    print(response)
