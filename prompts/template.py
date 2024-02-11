import json
import sys

system_message = """

与えられた商品内容から魅力的なキャッチコピーを生成してください。

## 制約
- 商品内容の情報から魅力的なキャッチコピーを一つ生成します
- 出力形式に従って生成してください

## 商品内容
商品名：{product_title}
商品説明：{product_description}

## 出力形式
{{キャッチコピー}}

""".strip()


if __name__ == "__main__":

    def generate_prompt(context: dict) -> str:
        return system_message.format(
            product_title=context["vars"]["product_title"],
            product_description=context["vars"]["product_description"],
        )

    print(generate_prompt(json.loads(sys.argv[1])))
