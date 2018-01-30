import json
import urllib
import boto3
import logging
import hype
import ast
import bsale


def urlToUtf8(url):
    utf8_urlencoded_key = url.encode('utf-8')
    key_utf8 = urllib.unquote_plus(utf8_urlencoded_key)
    key = key_utf8.decode('utf-8')
    return key


def selectRelevantData(data):
    product_resume = {}
    parameters = data.split('&')
    for p in parameters:
        if p.startswith('sku'):
            product_resume['sku'] = p.split('=')[1]
        if p.startswith('site_name'):
            product_resume['site_name'] = p.split('=')[1]
    return product_resume


def recoverIntegration(site_name):
    integration = {}

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('sitios_ondev')
    response = table.get_item(
        Key={
            'site_name': site_name
        }
    )

    if 'Item' not in response:
        logging.error(
            'Lo sentimos pero la integracion no se encuetra registrada')

        return {
            'status_code': 405,
            'content': {
                'status': 'Error',
                'message': 'integration not found'
            }
        }

    item = response['Item']
    integration['lp'] = item['loadingplay']
    integration['bsale'] = item['bsale']
    return integration


def validateProductIntegration(data):
    valid = False
    if 'status' in data:
        if data['status'] == 'success':
            product = data['product'][0]
            for tag in product['tags']:
                if tag['name'] == 'bsale':
                    valid = True
    return valid


def formatProductBsale(data):
    valid = False
    if 'status' in data:
        if data['status'] == 'success':
            product = data['product'][0]
            bsale_product_format = {
                'name': product['name'],
                'description': product['description']
            }
            valid = bsale_product_format
    return valid


def productIsOnBsale(client, data):
    isOnBsale = False
    request = client.Product.Get(limit=50, state=0)
    if request['count'] > 0:
        products = request['items']
        for prod in products:
            if prod['name'] == data['name']:
                isOnBsale = prod['id']
                break
    else:
        isOnBsale = False
    return isOnBsale


def sendProductToBsale(client_lp, client_bsale, product):
    # validar tag en el producto
    if validateProductIntegration(product):
        bsale_product = formatProductBsale(product)
        check_product = productIsOnBsale(client_bsale, bsale_product)
        # si existe el producto
        if not check_product:
            add_product = client_bsale.Product.Create(
                bsale_product['name'], bsale_product['description'])
            if 'id' in add_product:
                check_product = add_product['id']
        return check_product
    else:
        return False


def updateProductBsale():
    pass


def getVariantStock(client, cellar_id, sku):
    stock_value = False
    stock = client.Cellar.GetVariantStock(cellar_id, sku)
    if 'error' not in stock['status']:
        stock_value = stock['stock']['total']
    return stock_value
    pass


def formatCombinationToVariant(product_id, combination, variant_name, stock, price):
    variant = {
        'product_id': product_id,
        'name': variant_name,
        'combination': combination['sku'],
        'stock': stock,
        'price': price
    }

    return variant


def addVariantPrice(bsale_client, variant, price_list_id):
    pass


def addVariantStock(bsale_client, variant, office_id):
    pass


def formatToBsaleVariant(variant, data):
    if data['sku'] != variant['combination']:
        split_combination = variant['combination'].split('-')
        variant['name'] = variant['name'] + ' ' + split_combination[-1]

    variant = {
        'productId': variant['product_id'],
        'description': variant['name'],
        'code': variant['combination']
    }
    return variant


def updateVariantBsale():
    pass


def sendVariant(client_bsale, variant, data, price_list_id, office_id):
    variant_bsale = formatToBsaleVariant(variant, data)
    print variant_bsale
    create = client_bsale.Variant.Create(variant_bsale)
    if 'error' in create:
        # notify error in create
        # update variant
        pass
    else:
        # notify success in create
        add_price_bsale = addVariantPrice(bsale_client, create, price_list_id)
        # add price to price list
        add_stock_bsale = addVariantStock(bsale_client, create, price_list_id)
        # add stock to 
        pass

def saveStatus(data):
    pass


def proccessVariants(client_lp, client_bsale, data, product_id, product_price, cellar_id, price_list_id, office_id):
    variant_name = ''
    variant = client_lp.Variant.GetAll(data['site_name'], data['sku'])
    if len(variant['variants']) > 0:
        variant_name = variant['variants'][0]['name']

    combinations = client_lp.VariantCombination.GetAll(
        data['site_name'], data['sku'])

    if variant_name == '':
        name = client_lp.Product.Get(data['site_name'], data['sku'])
        variant_name = name['product'][0]['name']

    for comb in combinations['combination']:
        variant_stock = getVariantStock(client_lp, cellar_id, comb['sku'])
        if variant_stock:
            # hacer formateo de variante para bsale
            variant_bsale = formatCombinationToVariant(
                product_id, comb, variant_name, variant_stock, product_price)
            sendVariant(client_bsale, variant_bsale, data)
        else:
            # informar que la variante no se agregara a bsale debido
            # debido a que tiene stock
            pass

    pass


def hello(event, context):
    recived_product_data = event['body']
    formated_product_data = urlToUtf8(recived_product_data)
    relevant_product_data = selectRelevantData(formated_product_data)

    integration = recoverIntegration(relevant_product_data['site_name'])
    if 'status_code' in integration:
        # exit message and status
        pass
    else:
        if 'lp' in integration:
            lp_integration = ast.literal_eval(integration['lp'])
            client_lp = hype.API(lp_integration['token_lp'])
            bsale_integration = ast.literal_eval(integration['bsale'])
            client_bsale = bsale.API(bsale_integration['token_bsale'])

            product = client_lp.Product.Get(site_name=relevant_product_data['site_name'],
                                            sku=relevant_product_data['sku'])

            cellar_id = bsale_integration['cellar_id']
            price_list_id = bsale_integration['price_list_id']
            office_id = bsale_integration['office_id']

            sending_product = sendProductToBsale(
                client_lp, client_bsale, product)

            if sending_product:
                product_id = sending_product
                product_price = product['product'][0]['main_price']
                proccessVariants(client_lp, client_bsale, relevant_product_data,
                                 product_id, product_price, cellar_id, price_list_id, office_id)
                # notify faliure
                pass
            else:
                print sending_product


if __name__ == '__main__':
    event = {
        'body': 'bulk_price=0&sku=test_bsale_sin_var&bullet_1=Bullet+1&weight=0.0&bullet_3=Bullet+3&bullet_2=Bullet+2&description=Lorem+ipsum+dolor+sit+amet%2C+consectetur+adipiscing+elit.+Quisque+in+volutpat+ligula.+Quisque+vel+aliquam+erat.+Phasellus+finibus+turpis+quis+mauris+ultricies+facilisis.+Duis+efficitur+porttitor+nibh%2C+at+sollicitudin+tortor+vestibulum+at.+Duis+ullamcorper+lectus+arcu%2C+sed+congue+urna+egestas+eu.+Vivamus+commodo+metus+at+arcu+molestie+ultricies.+Pellentesque+finibus+ac+libero+ut+mattis.+Morbi+quis+augue+quam.+Etiam+placerat+et+elit+et+placerat.Cras+efficitur+molestie+quam+sit+amet+porttitor.+Sed+vitae+metus+efficitur%2C+interdum+augue+quis%2C+iaculis+metus.+Nullam+nec+purus+ultrices%2C+accumsan+turpis+at%2C+ullamcorper+nisi.+Duis+sed+sapien+quam.+Nam+quis+congue+quam.+Lorem+ipsum+dolor+sit+amet%2C+consectetur+adipiscing+elit.+In+iaculis+erat+erat%2C+vel+scelerisque+dolor+cursus+ut.+Donec+facilisis+finibus+lectus%2C+elementum+pharetra+erat+tempor+ac.+Mauris+tortor+nisl%2C+eleifend+vel+rutrum+quis%2C+pretium+vel+lacus.+Curabitur+bibendum+metus+felis%2C+sed+placerat+dolor+dictum+in.+Phasellus+iaculis+blandit+metus+vel+viverra.+Integer+id+gravida+lacus%2C+non+aliquet+enim.+Vivamus+dignissim+erat+eget+felis+pharetra+suscipit.+Vestibulum+sagittis+est+tellus%2C+eget+condimentum+dui+suscipit+sed.Duis+eu+nisl+eu+odio+ornare+varius+in+et+nulla.+In+ipsum+justo%2C+aliquam+vel+odio+sit+amet%2C+facilisis+bibendum+nibh.+Sed+iaculis+eu+erat+nec+finibus.+Integer+ac+urna+eget+quam+hendrerit+pulvinar.+Vestibulum+tristique+pulvinar+neque+tincidunt+malesuada.+Nullam+tincidunt+orci+vitae+mi+maximus%2C+id+faucibus+enim+sollicitudin.+Sed+id+dolor+eget+justo+pretium+facilisis.+Nulla+porttitor+odio+dapibus+est+bibendum+dignissim.+Donec+vitae+euismod+metus.Nam+porta%2C+augue+non+scelerisque+lacinia%2C+urna+urna+imperdiet+turpis%2C+a+sollicitudin+enim+lorem+ut+justo.+Vestibulum+eleifend+nisi+nec+urna+tincidunt%2C+a+sodales+diam+imperdiet.+Ut+tincidunt+ullamcorper+dolor.+Nunc+quis+risus+nisi.+Suspendisse+facilisis+mauris+massa%2C+eu+fermentum+quam+dictum+vel.+Vivamus+eu+cursus+elit.+Sed+facilisis+mi+sit+amet+dui+mollis+ullamcorper.Praesent+suscipit+ligula+a+dui+accumsan+blandit.+Maecenas+in+fringilla+nunc.+Nullam+faucibus+hendrerit+nibh+at+molestie.+Aenean+magna+sapien%2C+dictum+vel+vestibulum+et%2C+iaculis+ut+tortor.+Ut+placerat+libero+justo.+Fusce+maximus+nec+dolor+eu+pharetra.+Curabitur+et+lectus+nec+mauris+mollis+mattis+nec+molestie+risus.+Proin+at+nisi+ultrices%2C+auctor+dolor+ut%2C+congue+neque.+Ut+suscipit+sapien+pellentesque+ligula+porta%2C+in+facilisis+ex+ullamcorper.+Aliquam+quis+ultrices+justo.+In+hac+habitasse+platea+dictumst.+Phasellus+laoreet+feugiat+odio%2C+non+pretium+turpis+ultrices+id.+Phasellus+vitae+ipsum+ipsum.+Proin+felis+ante%2C+hendrerit+in+dignissim+sit+amet%2C+cursus+id+nisl.Praesent+sit+amet+faucibus+nisl.+Phasellus+vitae+laoreet+ipsum.+Nullam+ornare+condimentum+aliquam.+Aenean+sit+amet+malesuada+dolor.+Donec+eget+elit+lacus.+Sed+eu+dolor+eu+ex+fermentum+rhoncus.+In+massa+justo%2C+euismod+quis+justo+nec%2C+pretium+lobortis+est.+Duis+dignissim%2C+dolor+ac+tincidunt+blandit%2C+lorem+lacus+placerat+ante%2C+vitae+lobortis+turpis+ex+et+massa.+Aliquam+sit+amet+vulputate+ante%2C+id+placerat+mauris.Sed+malesuada+aliquet+dapibus.+Nam+euismod+luctus+lacinia.+In+quis+lacinia+mi.+Lorem+ipsum+dolor+sit+amet%2C+consectetur+adipiscing+elit.+Quisque+tempus+purus+nec+nibh+scelerisque+pulvinar.+Duis+sed+arcu+pulvinar%2C+euismod+diam+et%2C+suscipit+lorem.+Interdum+et+malesuada+fames+ac+ante+ipsum+primis+in+faucibus.+Aenean+id+mauris+vehicula%2C+posuere+arcu+ac%2C+finibus+turpis.+Nulla+felis+neque%2C+fringilla+tempor+congue+ut%2C+imperdiet+sed+nisi.Praesent+risus+est%2C+ornare+nec+vehicula+id%2C+imperdiet+at+risus.+Curabitur+vestibulum+non+odio+vel+pharetra.+Integer+convallis+dignissim+diam+non+dictum.+Donec+augue+tortor%2C+vehicula+ac+neque+vel%2C+aliquam+rhoncus+lacus.+Nulla+vel+fermentum+mauris.+Cras+faucibus+quis+est+a+tincidunt.+Sed+imperdiet+in+quam+in+commodo.+Praesent+ut+nulla+fringilla%2C+lacinia+neque+non%2C+consequat+leo.+Etiam+in+nulla+malesuada+quam+euismod+semper+non+a+quam.Curabitur+vitae+ligula+vel+mi+feugiat+fringilla.+Nunc+sagittis+nulla+eget+nisl+pellentesque+dignissim.+Proin+quis+metus+et+eros+dignissim+laoreet+id+vel+purus.+Ut+non+purus+a+nulla+convallis+volutpat+nec+sed+felis.+Cras+vel+neque+euismod%2C+elementum+lorem+in%2C+maximus+justo.+Proin+euismod+ligula+libero%2C+id+malesuada+arcu+finibus+vitae.+Aliquam+erat+volutpat.+Cras+purus+sem%2C+pretium+nec+malesuada+eu%2C+viverra+at+dui.+Aliquam+dictum+consequat+fermentum.+Morbi+risus+ex%2C+laoreet+quis+venenatis+sit+amet%2C+tincidunt+et+ex.+Nunc+accumsan%2C+felis+vel+lobortis+ornare%2C+quam+quam+luctus+ipsum%2C+et+ornare+elit+felis+sit+amet+velit.+Cum+sociis+natoque+penatibus+et+magnis+dis+parturient+montes%2C+nascetur+ridiculus+mus.Ut+elementum+tortor+quis+arcu+malesuada%2C+a+malesuada+urna+rhoncus.+Duis+consequat+tincidunt+consectetur.+Nam+ac+sapien+a+odio+tempus+commodo.+Morbi+sollicitudin+commodo+turpis%2C+a+gravida+ex+dignissim+nec.+Sed+malesuada+nisl+eget+laoreet+molestie.+Suspendisse+potenti.+Morbi+interdum+urna+a+diam+venenatis%2C+et+tristique+metus+vestibulum.+Vivamus+tincidunt+urna+quis+pellentesque+posuere.+Vivamus+egestas+purus+non+feugiat+egestas.Fusce+enim+sem%2C+dictum+ac+congue+sed%2C+dictum+id+dolor.+Cras+a+scelerisque+nunc.+Duis+vitae+lectus+non+eros+tincidunt+tempor.+Maecenas+interdum+finibus+tellus+nec+porttitor.+Sed+massa+quam%2C+facilisis+sed+ipsum+at%2C+pharetra+convallis+erat.+Phasellus+elementum%2C+diam+a+maximus+bibendum%2C+nisi+turpis+dignissim+enim%2C+ut+lobortis+arcu+sapien+id+magna.+Fusce+quis+velit+id+sapien+aliquet+viverra+ac+pharetra+nulla.+Morbi+vel+vestibulum+ligula.Ut+est+massa%2C+sollicitudin+ut+porttitor+eget%2C+fermentum+non+lectus.+Vestibulum+vestibulum+condimentum+orci%2C+et+porttitor+arcu+venenatis+id.+Donec+aliquam+convallis+vestibulum.+Nulla+porta+commodo+dui+sit+amet+fermentum.+Sed+eget+accumsan+elit.+Integer+vel+tristique+augue.+In+porttitor+ipsum+at+libero+posuere+ultrices.+Donec+scelerisque+tellus+risus%2C+in+lobortis+nunc+dictum+vel.+Proin+nec+quam+facilisis+justo+feugiat+tincidunt.+Ut+ex+libero%2C+laoreet+eu+sem+at%2C+scelerisque+commodo+elit.+Sed+et+libero+non+nibh+lobortis+auctor+vel+a+augue.Proin+congue+nulla+non+rhoncus+tempus.+Morbi+finibus+erat+lorem%2C+at+placerat+diam+tincidunt+in.+In+hac+habitasse+platea+dictumst.+Aliquam+diam+dui%2C+finibus+fringilla+turpis+eu%2C+egestas+tempus+augue.+Sed+nunc+dui%2C+rhoncus+vel+turpis+nec%2C+pellentesque+ultricies+velit.+Fusce+egestas+mollis+gravida.+Duis+at+risus+nec+elit+porttitor+volutpat.+Etiam+ultricies+ipsum+ante%2C+ut+commodo+felis+gravida+congue.+Vestibulum+scelerisque+odio+ut+ipsum+pellentesque+placerat.+Proin+fringilla+vestibulum+sapien.+Fusce+sollicitudin+diam+massa%2C+quis+aliquet+dolor+fermentum+nec.Vivamus+eget+nibh+vestibulum%2C+molestie+mauris+non%2C+aliquam+mauris.+Aenean+scelerisque+enim+nec+mi+dictum+hendrerit.+Vivamus+venenatis+tellus+tristique%2C+euismod+diam+ut%2C+imperdiet+enim.+Morbi+blandit+dui+non+libero+finibus+molestie.+In+pulvinar+volutpat+accumsan.+Etiam+ut+eleifend+urna.+Mauris+commodo%2C+massa+id+blandit+accumsan%2C+ligula+tortor+auctor+felis%2C+a+euismod+elit+arcu+in+quam.+Curabitur+laoreet+facilisis+facilisis.+Aliquam+erat+volutpat.+Etiam+auctor+aliquam+eros.+Ut+ullamcorper+odio+vitae+tortor+ultrices%2C+ac+finibus+ligula+tincidunt.+Quisque+tempor+ac+magna+id+vehicula.Aliquam+massa+nisi%2C+faucibus+at+nulla+ac%2C+consectetur+consectetur+turpis.+Fusce+tellus+nisi%2C+accumsan+ut+ipsum+ac%2C+pretium+pretium+leo.+Curabitur+nec+ipsum+pulvinar%2C+venenatis+odio+sit+amet%2C+commodo+metus.+Phasellus+sed+ornare+diam.+Maecenas+dolor+enim%2C+finibus+sed+vehicula+eu%2C+semper+non+ante.+Suspendisse+ut+odio+nec+enim+suscipit+dignissim.+Maecenas+risus+quam%2C+accumsan+at+urna+consectetur%2C+pellentesque+consectetur+leo.+Nam+ex+enim%2C+egestas+eget+nisi+imperdiet%2C+eleifend+aliquam+risus.+Praesent+porta+urna+eget+justo+fermentum+tincidunt.&site_id=29&name=Lorem+ipsum+dolor+sit+amet%2C+consectetur+adipiscing+elit.+Quisque+in+volutpat+ligula.&for_sale=0&in_stock=True&site_name=test&upp=1&main_price=542352.0&position=0&critical_stock=1&manufacturer=&brand=&promotion_price=0.0&cost_price=0', 'resource': '/users/create', 'requestContext': {
            'requestTime': '18/Jan/2018:20:13:02 +0000',
            'protocol': 'HTTP/1.1',
            'resourceId': 'tvjqla',
            'apiId': 'b2j4ukoe05',
            'resourcePath': '/users/create',
            'httpMethod': 'POST',
            'requestId': 'fc7aa860-fc8b-11e7-94f4-65c399a15f53',
            'path': '/dev/users/create',
            'accountId': '456187946960',
            'requestTimeEpoch': 1516306382465,
            'identity': {
                'userArn': None,
                'cognitoAuthenticationType': None,
                'accessKey': None,
                'caller': None,
                'userAgent': 'python-requests/2.18.4',
                'user': None,
                'cognitoIdentityPoolId': None,
                'cognitoIdentityId': None,
                'cognitoAuthenticationProvider': None,
                'sourceIp': '165.227.179.126',
                'accountId': None
            },
            'stage': 'dev'
        }, 'queryStringParameters': None, 'httpMethod': 'POST', 'pathParameters': None, 'headers': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Via': '1.1 efdf33ba79ee3aadbfdf7e2b6e838d71.cloudfront.net (CloudFront)',
            'Accept-Encoding': 'gzip, deflate',
            'CloudFront-Is-SmartTV-Viewer': 'false',
            'CloudFront-Forwarded-Proto': 'https',
            'X-Forwarded-For': '165.227.179.126, 205.251.250.44',
            'CloudFront-Viewer-Country': 'US',
            'Accept': '*/*',
            'User-Agent': 'python-requests/2.18.4',
            'X-Amzn-Trace-Id': 'Root=1-5a60ffce-0c0a9f0a5b9814f159da7292',
            'Host': 'b2j4ukoe05.execute-api.us-east-1.amazonaws.com',
            'X-Forwarded-Proto': 'https',
            'X-Amz-Cf-Id': 'BobFYbgNyHsK0TMQNKGmkJXMbOAg-K5IVJDD9p1rTgSBwj-GgnvgkQ==',
            'CloudFront-Is-Tablet-Viewer': 'false',
            'X-Forwarded-Port': '443',
            'CloudFront-Is-Mobile-Viewer': 'false',
            'CloudFront-Is-Desktop-Viewer': 'true'
        }, 'stageVariables': None, 'path': '/users/create', 'isBase64Encoded': False
    }
    hello(event, {})
