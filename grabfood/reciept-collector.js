function grabFoodReceipt() {
  var foodLabel = GmailApp.getUserLabelByName('grabfood');
  var claimedLabel = GmailApp.getUserLabelByName('grabfood-claimed');
  var threads = foodLabel.getThreads();
  for (var i = threads.length - 1; i >= 0; i--) {
    var messages = threads[i].getMessages();
    for (var j = messages.length - 1; j >= 0; j--) {
      var message = messages[j];
      var month = Utilities.formatDate(message.getDate(), 'GMT+7', 'MM/yyyy');
      var fileIdKey = 'fileId-' + month;
      var totalAmountKey = 'totalAmount-' + month;
      var fileName = 'grabfood-' + month + '.html';
      var fileId = PropertiesService.getScriptProperties().getProperty(fileIdKey);
      var document;
      var totalAmount;
      if (fileId == null) {
        document = DriveApp.createFile(fileName, '', 'text/html');
        totalAmount = 0;
        PropertiesService.getScriptProperties().setProperty(fileIdKey, document.getId());
        PropertiesService.getScriptProperties().setProperty(totalAmountKey, '0');
      } else {
        document = DriveApp.getFileById(fileId);
        if (document == null) {
          throw 'document for month ' + month + ' not found';
        }
        totalAmount = parseInt(PropertiesService.getScriptProperties().getProperty(totalAmountKey));
        if (totalAmount == NaN) {
          throw 'current total amount of month ' + month + ' is invalid';
        }
      }

      var content = document.getBlob().getDataAsString();
      var amount = parseInt(getTotalAmount(message.getBody()));
      if (amount == NaN) {
        throw "Can't get receipt amount";
      }
      content +=
        message.getBody().replace('ISO-8859-1', 'UTF-8') +
        '<div style="margin: 5px auto; text-align: center;">' +
        totalAmount +
        ' + ' +
        amount +
        ' = ';
      totalAmount = totalAmount + amount;
      PropertiesService.getScriptProperties().setProperty(totalAmountKey, totalAmount.toString());
      content += totalAmount + '</div>';
      document.setContent(content);
    }
    threads[i].addLabel(claimedLabel);
    threads[i].removeLabel(foodLabel);
  }
}

function getTotalAmount(email) {
  return /">VND (\d+)/g.exec(email)[1];
}