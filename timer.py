import time

def get_timestamp() -> float:
    """
    获取当前时间戳
    
    Returns:
        float: 当前时间的UNIX时间戳(秒)
    """
    return time.time()

def get_formatted_time() -> str:
    """
    获取格式化的当前时间字符串
    
    Returns:
        str: 格式化的时间字符串,格式为'YYYY-MM-DD HH:MM:SS'
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
