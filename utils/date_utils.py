from datetime import datetime


def format_date(date_str):
    try:
        # 解析原始日期字符串
        date_obj = datetime.strptime(date_str, '%I:%M%p %b %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date
    except ValueError:
        return date_str