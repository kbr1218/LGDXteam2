# is_watched.py
from setup import load_views_vectorstore, views_vectorstore

def is_watched(user_id: str, asset_id: str) -> bool:
    global views_vectorstore
    """
    views_vectorstore에서 사용자의 특정 asset_id 시청 여부 확인
    
    Args:
      user_id (str): 사용자 ID
      asset_id (str): 조회할 asset ID

    Returns:
      bool: 시청했다면 True, 시청하지 않았다면 False
    """
    if views_vectorstore is None:  # ✅ 벡터스토어가 로드되지 않았으면 로드
        print("🔄 벡터스토어가 None임 새로 로드 (is_watched.py)")
        views_vectorstore = load_views_vectorstore(user_id)
    
    watched_results = views_vectorstore.similarity_search(
      query="",
      k=1,
      filter={"$and": [
          {"user_id": {"$eq": user_id}}, 
          {"asset_id": {"$eq": asset_id}}
      ]}
    )
    
    return len(watched_results) > 0