from rest_framework import serializers

from Friendship.models import SearchAccount, Request


class SearchAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchAccount
        fields = ['gender', 'grade']

    def save(self, **kwargs):
        account = SearchAccount(user=self.context['request'].user,
                                gender=self.validated_data['gender'],
                                grade=self.validated_data['grade'])
        account.save()
        return account


class SendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ['receiver', 'subject']

    def save(self, **kwargs):
        request = Request(sender=self.context['request'].user,
                          receiver_id=self.validated_data['receiver'],
                          subject_id=self.validated_data['subject'])
        request.save()
        return request


class GetRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ['sender', 'state', 'created_time', 'subject']

