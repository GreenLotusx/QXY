import hashlib
import hmac


def check_num_maxmin(iNum,iMax,iMin):
    """
    检查传入值是否在指定区间内
    :param iNum: 检测值
    :param iMax: 最大值
    :param iMin: 最小值
    :return: 布尔类型结果True或False
    """
    if iMax<iMin:
        iMax,iMin = iMin,iMax
    if iNum > iMax or iNum < iMin:
        return False
    return True


def hmac_sha256_single(str):
    """
    hmacsha256加密
    :param str: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    return hmac.new(str.encode("utf-8"), digestmod=hashlib.sha256).hexdigest().upper()