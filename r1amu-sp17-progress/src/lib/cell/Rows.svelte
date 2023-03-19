<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        @apply flex flex-row;
    }
</style>
